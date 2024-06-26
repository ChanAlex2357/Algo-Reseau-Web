import tkinter as ttk
from tkinter.constants import *

import gui.graphpanel
import gui.layout
from .formulaire.server import ServerFormulaire
from .formulaire.liaison import LiaisonFormulaire
from .formulaire.site import SiteFormulaire
from gui.layout.server import ServerLayout
import gui
from .recherche import RecherhePanel
from gui.layout.liaison import LiaisonLayout

class GraphPanel(ttk.Frame):
    def __init__(self,
                window,
                dns,
                servers:list=list(),
                liaisons:list=list()
    ):
        super().__init__(window,width=1980)
        self.pack(side=LEFT,expand=YES,fill=BOTH)
        self.window = window
        self.servers = servers
        self.dns = dns
        self.liaisons = liaisons
        self.recherhe_panel = RecherhePanel(self,dns)
        self.menu = None
        self.server_menu = None
        # Creation du canevas
        self.canevas = self.create_canevas()
        
        # Integrer les servers de base
        self.integrate_servers(self.servers)
        self.integrate_liaisons(self.liaisons)

    ''' Creation d'un canevas qui sera utiliser pour faire la representation des graphs 
    
        Return
            objet de type tkinter.Canevas pour representer les graphs 
    '''
    def create_canevas(self):
        # Creation du canevas de graph a visualiser
        canevas = ttk.Canvas(self,bg="white")
        canevas.pack(fill=BOTH,expand=YES)
        # Ajouter le listner du canevas pour afficher le menu 
        canevas.bind("<Button-3>",self.pop_menu)
        from gui.application import Application
        canevas.bind("<ButtonPress-1>", lambda event: Application.controlpanel.server_detail_panel.release_content())
        return canevas

    '''Creation d'un menu de choix d'actions lors d'un clic droit
        Args
            Les donnees de l'evenement
        Return 
            Le menu a afficher en clic droit
    '''
    def create_menu(self,x,y):
        menu = ttk.Menu(self, tearoff=0)
        params = (x,y)
        # Creation d'un formulaire pour un server qui sera placer en x,y du clic 
        func = lambda: self.create_server_formulaire(*params)
        menu.add_command(label="add server", command = func)
        return menu

    ''' Afficher le Menu de choix lors d'un clic droit
        Args
            Les donnees de l'evenement
    '''
    def pop_menu(self,event):
        x = event.x_root
        y = event.y_root
        if self.menu == None:
            self.menu = self.create_menu(x,y)
        self.menu.post(x,y)
    def unpop_menu(self):
        self.canevas.dtag(self.menu)
        self.menu = None 
    
    '''Creation d'une fenetre de formulaire pour cree un nouveau server
        Args
            x,y les coordonness pour sa representation graphique
    '''
    def create_server_formulaire(self,x,y):
        master = ttk.Tk()
        master.title("Formulaire Server")
        # Creation d'une fenetre de formulaire
        ServerFormulaire(
            master,
            self,
            x,y
        )

    ''' Ajout d'un server dans le canevas de visualisation
    '''
    def add_server(self,server,x,y):
        self.remove_graph(server) 
        # Creation de la representation du server
        serverLayout = ServerLayout(self,server,x,y)
        server.set_layout(serverLayout)

    '''Ajouter une liaison dans le canevas par son layout
        Args:
            liaison a afficher/ajouter dans le canevas
    '''
    def add_liaison(self,liaison):
        self.remove_graph(liaison)
        # Cree la representaion de la liaison
        if liaison.get_etat() :
            layout = LiaisonLayout(self,liaison)
            liaison.set_layout(layout)
    
    def integrate_servers(self,servers:list):
        x = 0 
        y = 0
        for server in servers:
            self.add_server(server,x,y)
            x += 10
            y += 10
    
    def integrate_liaisons(self,liaisons:list):
        for liaison in liaisons:
            self.add_liaison(liaison)
    def reintegrate_liaisons(self):
        self.integrate_liaisons(self.liaisons)
    def reintegrate_servers(self):
        self.integrate_servers(self.servers)

    def reset_hilight(self):
        for server in self.servers:
            try :
                server.get_layout().unhilight()
            except AttributeError:
                pass;
        for liaison in self.liaisons:
            try :
                liaison.get_layout().unhilight()
            except AttributeError:
                pass;

    def hilight_on_graph(self,graph,color="red",reset=False):
        if reset :
            self.reset_hilight()
        graph.hilight(color)

    def remove_graph(self,graph_object:gui.layout.GraphLayout):
        coords = list
        if graph_object.get_layout() is not None:
            # coords.append( graph_object.get_x())
            # coords.append( graph_object.get_y())
            graph_object.get_layout().remove_layout()
        return coords


    def remove_graphs(self):
        for server in self.servers:
            self.remove_graph(server)
        for liaison in self.liaisons:
            self.remove_graph(liaison)

    def reintegrate_graphs(self):
        self.reintegrate_servers()
        self.reintegrate_liaisons()

    def refresh_graphs(self):
        self.reintegrate_graphs()

    def create_liaison_form(self,server):
        master = ttk.Tk()
        master.title("Formulaire liaison")
        from gui.application import Application 
        LiaisonFormulaire(master, self , server)

    def create_site_form(self,server):
        master = ttk.Tk()
        master.title("Formulaire site")
        from gui.application import Application 
        SiteFormulaire(master, self , server)

    def create_server_menu(self,server):
        menu = ttk.Menu(self, tearoff=0)
        params = (server)
        from gui.application import Application
        liaison = lambda : Application.controlpanel.server_detail_panel.add_liaison(server)
        site = lambda : Application.controlpanel.server_detail_panel.add_site(server)
        kill = lambda : self.kill_server(server)
        start = lambda : self.launch_server(server)
        # Creation d'un formulaire pour un server qui sera placer en x,y du clic
        menu.add_command(label="add liaison", command = liaison)
        menu.add_command(label="add site", command = site)
        menu.add_command(label="kill", command = kill)
        menu.add_command(label="start", command = start)

        return menu
    def pop_server_menu(self,x,y,server):
        if self.server_menu != None:
            self.server_menu.destroy()
        self.server_menu = self.create_server_menu(server)
        self.server_menu.post(x,y)
        self.unpop_menu()
    def kill_server(self,server):
        server.shutdown()
        self.refresh_graphs()
    def launch_server(self,server):
        server.start()
        self.refresh_graphs()

