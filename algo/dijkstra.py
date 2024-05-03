from network.server import Server

'''Represente un sommet de server pour l'algo de dijkstra'''
class Checkout():
    def __init__(self,server,parent=None,value=None):
        self.server = server
        self.value = value
        self.parent = parent
        self.finished = False

    def __str__(self):
        return f"Checkout of {self.server.get_adresse_ip()} "
    
    '''Changer l'etat du checkout en fini'''
    def set_done(self):
        self.finished = True

    ''' Indique si le checkout a deja ete traiter ou non selon la valeur de son etat'''
    def is_finished(self):
        return self.finished
        
    '''Recupere le checkout d'un server parmi une liste de checkouts
        ARGS
            server : le server du checkout
            checkouts : la liste des checkouts
    '''
    @classmethod
    def get_checkout_of(cls,server:Server,checkouts:list):
        
        for chk in checkouts :
            # tester l'identite du server de checkout chk
            if chk.server.get_adresse_ip() == server.get_adresse_ip():
                return chk
        # Si le checkout n'existe pas on va le cree
        new_checkout = cls(server)
        # Ajouter le nouveau checkout dans la liste
        checkouts.append(new_checkout)
        return new_checkout

'''Represente le chemin d'accees vers un server a partir d'un checkout final''' 
class ServerPath():
    def __init__(self,checkout):
        pass

def find_short_path(server_depart , server_arrivee , servers:list ):
    # La liste des checkouts pour 
    checkouts = list()
    # Initalisation des checkouts pour chaque server
    for server in servers :
        Checkout.get_checkout_of(server,checkouts)
    # Recuperer le checkout de depart
    origin_checkout = Checkout.get_checkout_of(server_depart,checkouts)
    # Configurer la  valeur en tant que 0
    origin_checkout.value = 0
    # La file de tratement
    sources = [origin_checkout]
    # Tant la fil de tratement n'est pas vide on continue
    while sources.__len__() > 0:
        # Faire le traitements des sources et prendres la liste resultante comme prochaine source 
        sources = sources_traitement(sources,checkouts)
    final_checkout = Checkout.get_checkout_of(server_arrivee,checkouts)
    return ServerPath(final_checkout)

'''Fait le traitement d'une liste de sources de memes niveaux et etablir qui seront les suivants
    ARGS:
        sources : la liste des sources
        checkoouts : la liste des checkouts
    RETURN:
        temp_sources : la liste ordonnee croissante des sources suivantes
'''
def sources_traitement(sources,checkouts):
    temp_sources = set()
    # Traiter les checkouts_source de meme niveau
    for source_checkout in sources:
        # Pour chaque source les checkout suivants seront dans temp_sources
        checkout_traitement(source_checkout,temp_sources,checkouts)
    # reorganiser la file pour que celle qui a la valeur la plus petite passe en premier
    temp_sources = sorted(temp_sources,key=lambda obj: obj.value,reverse=True)
    return temp_sources

'''Fait le traitement d'un checkout en introduisant ses voisins dans la file des sources
    ARGS
        source_checkout : la source a traiter
        temp_sources : la liste pour les voisins qui suivrons
        checkouts : la liste de touts les checkouts
'''
def checkout_traitement(source_checkout,temp_sources:set,checkouts):
    # Recuperation du checkout a traiter et son server attribuer
    source_server = source_checkout.server

    for liaison in source_server.get_lisaisons():
        # pour chaque server lier au source on fait son traitement checkout
        server_voisin = liaison.get_server_lier(source_server)
        checkout_voisin = Checkout.get_checkout_of(server_voisin,checkouts)
        # Ne pas traiter le checkout si elle est deja finie
        # Mais faire le traitement si elle n'est pas encore tratiee
        if not checkout_voisin.is_finished():
            # Calculer la valeur de test ; value = valeur du parent + le temps de response de la liaison
            value = source_checkout.value + liaison.get_temps_reponse()
            # Test de changement de valeur
            # la valeur None est considere comme infinie
            if (checkout_voisin.value == None) or (checkout_voisin.value > value):
                # Remplacer la valeur par la valeur du parent qui est plus petite
                checkout_voisin.value = value
                # Considerer le checkout de la source comme le parent de ce checkout
                checkout_voisin.parent = source_checkout
            # ajouter le chekout voisin dans la file de source a venir
            temp_sources.add(checkout_voisin)
    # Changer l'etat du checkout source
    source_checkout.set_done()