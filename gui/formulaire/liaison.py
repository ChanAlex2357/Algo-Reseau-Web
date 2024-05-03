import tkinter as ttk
from tkinter.constants import *
import gui.helpers as ghelp
from network.server import Server
class LiaisonFormulaire(ttk.Frame):
    def __init__(self,master,graphpanel,serverBase:Server):
        super().__init__(master)
        self.graphpanel = graphpanel
        self.pack(fill=BOTH,expand=YES,padx=20,pady=10)

        # declarations des champs du formulaire
        # L'adresse du server
        value:str = ""
        server1Ip = ttk.StringVar(value=value)
        self.server1Ip_entry = ghelp.create_form_entry(self,"Server1 Ip : ",server1Ip)
        if serverBase is not None :
            value = serverBase.get_adresse_ip()
            self.server1Ip_entry.insert(0,value)

        server2Ip = ttk.StringVar(value="")
        self.server2Ip_entry = ghelp.create_form_entry(self,"Server2 Ip : ",server2Ip)
        
        delay = ttk.IntVar(value=0)
        self.delay_entry = ghelp.create_form_entry(self,"dstance : ",delay)
        
        # Le button de validation de l'ajout
        self.submitButton = ghelp.create_submit_button(self,"Ajouter",self.create_liaison)
    
    ''' Creation d'une liaison selon les donnees remplit en formulaire
    et cree sa representation dans le grand canevas des graphs

        Args
        x , y : la position du representation graphique de la liaison 
    '''
    def create_liaison(self):
        # Recuperation des donnees
        ip1 = self.server1Ip_entry.get()
        ip2 = self.server2Ip_entry.get()
        delay = self.delay_entry.get()
        from gui.application import Application
        server1 = Application.findServer(ip1)
        server2 = Application.findServer(ip2)
        liaison = server1.add_liaison(server2,delay)
        if liaison == None :
            print ("liaison already exist")
            return
        print(f"{ip1} -- {delay} -- {ip2}")
        # Ajouter la liaison  dans la liste des liaison de l'application
        self.graphpanel.liaisons.append(liaison)
        # Donner la liaison au graph pour etre integrer dans l'affichage
        self.graphpanel.add_liaison(liaison)

