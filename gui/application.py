import tkinter as ttk
from tkinter.constants import *
from .controlpanel import ControlPanel
from .graphpanel import GraphPanel
from network.dns import Dns
# Declaration des objets a manipuler
class Application(ttk.Tk):
    dns:Dns
    servers:list
    liaisons:list
    graphpanel:GraphPanel
    controlpanel:ControlPanel
    def __init__(self,
                 dns = Dns(),
                 servers=list(),
                 liaisons=list()
        ):
        super().__init__();
        Application.dns = dns
        Application.servers = servers
        Application.liaisons = liaisons
        # Configuration de la fenetre
        self.title("Web Reseau")
        # La partie de l'affichage pour controller les doneess
        Application.controlpanel = ControlPanel(self,dns,servers,liaisons)
        # La partie qui gere la representation des donnees
        Application.graphpanel = GraphPanel(self,dns,servers,liaisons)

    '''Demarrage de l'applcation
    '''
    def run(self):
        self.mainloop()
    
    '''Trouver un server dans la liste des servers grace a son adresse ip
        Args
         - ip : l'adresse ip du server a trouver
        
        Return
            - le server portant l'adresse ip 
            - sinon None quand le server n'existe pas
    '''
    def findServer(ip:str):
        for server in Application.servers:
            if server.get_adresse_ip() == ip:
                return server
        return None
    