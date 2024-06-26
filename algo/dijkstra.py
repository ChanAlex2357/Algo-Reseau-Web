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
        self.server_arrivee = checkout.server
        self.value = checkout.value
        self.set_servers_suites(checkout)
        
    def __str__(self):
        string = ""
        for server in self.servers_suite :
            string += f"{server.get_adresse_ip()} --> "
        string += f"|{self.value}|"
        return string 
    
    def set_servers_suites(self,checkout):
        servers = [checkout.server,]
        parent = checkout.parent
        while parent is not None :
            servers.insert(0,parent.server)
            self.server_depart = parent
            parent = parent.parent
        self.servers_suite = servers 

    def hilight(self,color="red"):
        servers = self.servers_suite
        for i in range(len(servers)) :
            server = servers[i]
            server.get_layout().hilight(color)
            try :
                liaison = server.get_liaison_with(servers[i+1])
                liaison.get_layout().hilight(color)
            except IndexError:
                pass;


def parcour_en_largeur(server_depart:Server,servers:list):
    check_depart = Checkout(server=server_depart,value=0)
    checkouts = list()
    checkouts.append(check_depart)
    visited = list()
    visited.append(server_depart)

    file_ = list()

    file_.append(server_depart)
    while len(file_) > 0:
        curr = list()
        for v in file_:
            check_v = Checkout.get_checkout_of(v,checkouts)
            for liaison in v.get_lisaisons():
                if not liaison.get_etat() :
                    continue
                u = liaison.get_server_lier(v)
                if u not in visited :
                    visited.append(u)
                    value = check_v.value + 1
                    check_voisin = Checkout(server=u,parent=check_v,value=value)
                    curr.append(u)
                    checkouts.append(check_voisin)
        for vis in visited:
            try :
                file_.remove(vis)
            except Exception:
                pass
        for value in curr:
            file_.append(value)
    return checkouts
            
def find_path_en_largeur(server_depart:Server , server_arrivee , servers:list ):
    checkouts = parcour_en_largeur(server_depart,servers)
    check_arrive = Checkout.get_checkout_of(server_arrivee,checkouts)
    return ServerPath(check_arrive)


def find_short_path(server_depart:Server , server_arrivee , servers:list ):
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
        # Verifier si la liaison est active
        if not liaison.get_etat() :
            continue
        # pour chaque server lier au source on fait son traitement checkout
        server_voisin = liaison.get_server_lier(source_server)
        checkout_voisin = Checkout.get_checkout_of(server_voisin,checkouts)
        # Ne pas traiter le checkout si elle est deja finie
        # Mais faire le traitement si elle n'est pas encore tratiee
        if not checkout_voisin.is_finished():
            # Calculer la valeur de test ; value = valeur du parent + le temps de response de la liaison
            value = source_checkout.value + int(liaison.get_temps_reponse())
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