import tkinter as ttk
from tkinter.constants import *
import gui.helpers as ghelp
from web.site import Site
from network.server import Server

class SiteFormulaire(ttk.Frame):
    def __init__(self,master,graphpanel,serverBase:Server):
        super().__init__(master)
        self.graphpanel = graphpanel
        self.pack(fill=BOTH,expand=YES,padx=20,pady=10)

        # declarations des champs du formulaire
        # L'adresse du server
        value:str = ""
        serverIp = ttk.StringVar(value=value)
        self.serverIp_entry = ghelp.create_form_entry(self,"Ip Server : ",serverIp)
        if serverBase is not None :
            value = serverBase.get_adresse_ip()
            self.serverIp_entry.insert(0,value)
        domaine = ttk.StringVar(value="")
        self.domaine_entry = ghelp.create_form_entry(self,"Nom du site : ",domaine)
        content = ttk.StringVar(value="")
        self.content_entry = ghelp.create_form_entry(self,"Contenu : ",content)
        # Le button de validation de l'ajout
        self.submitButton = ghelp.create_submit_button(self,"Ajouter",self.create_site)
    
    ''' Creation d'un site selon les donnees remplit en formulaire
    et cree sa representation dans le grand canevas des graphs

        Args
        x , y : la position du representation graphique du site 
    '''
    def create_site(self):
        # Recuperation des donnees
        ip = self.serverIp_entry.get()
        domaine = self.domaine_entry.get()
        content = self.content_entry.get()
        # Recuperation du server concernee
        from gui.application import Application
        server = Application.findServer(ip)
        # Essaye d'ajout et creation du site dans le server 
        site = server.add_site(domaine,content)
        # Verfier si le site a bien ete cree ou non
        if site == None :
            print ("site already exist")
            return
        from gui.application import Application
        Application.controlpanel.server_detail_panel.update_content(server)
  
