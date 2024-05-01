import tkinter as ttk
from tkinter.constants import *
import gui.helpers as ghelp
from network.server import Server
from gui.layout.server import ServerLayout

class ServerFormulaire(ttk.Frame):
    def __init__(self,master,graphpanel,servers,x,y):
        super().__init__(master)
        self.servers  = servers
        self.graphpanel = graphpanel

        self.pack(fill=BOTH,expand=YES,padx=20,pady=10)

        # declarations des champs du formulaire
        # Le nom du server
        serverName =  ttk.StringVar(value="")
        self.serverName_entry = ghelp.create_form_entry(self,"Server Name : ",serverName)
        
        # L'adresse du server
        serverIp = ttk.StringVar(value="")
        self.serverIp_entry = ghelp.create_form_entry(self,"Adresse Ip : ",serverIp)
        
        # Le button de validation de l'ajout
        self.submitButton = ghelp.create_submit_button(self,"Ajouter",self.create_submit_function(x,y))
    
    ''' Creation d'un server selon les donnees remplit en formulaire
    et cree sa representation dans le grand canevas des graphs

    Args
        x , y : la position du representation graphique du server 
    '''
    def create_server(self,x,y):
        # Recuperation des donnees
        serverName = self.serverName_entry.get()
        adresseIp = self.serverIp_entry.get()
        # Creation de l'objet server
        server = Server(serverName,adresseIp,self.graphpanel.dns)
        # Ajouter le server au liste des servers
        self.graphpanel.servers.append(server)
        # Creation de la representation du server
        serverLayout = ServerLayout(self.graphpanel,server,x,y)
        self.master.winfo_exists()
        
    '''Creation d'un objet fonction qui sera executer une fois le formulaire valider
        Args
            x,y position de la representaiton du server a cree
        Return
            La fonction de validation de creation d'un server  
    '''
    def create_submit_function(self,x,y):
        params = (x,y)
        func = lambda: self.create_server(*params)
        return func
