import tkinter as ttk
from tkinter.constants import *
from .formulaire.server import ServerFormulaire

class GraphPanel(ttk.Frame):
    def __init__(self,window,dns,servers:list=list()):
        super().__init__(window,width=1980,)
        self.pack(side=TOP ,expand=YES,fill=BOTH)
        self.window = window
        self.servers = servers
        self.dns = dns
        # Creation du canevas
        self.canevas = self.create_canevas()

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
        menu = self.create_menu(x,y)
        menu.post(x,y)
    
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
            self.servers,
            x,y
        )