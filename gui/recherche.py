import tkinter as ttk
from tkinter.constants import *
import gui.helpers as ghelp
import algo.dijkstra as dijkstra
class RecherhePanel(ttk.Frame):
    def __init__(self,window,dns):
        super().__init__(window)
        self.dns = dns
        self.pack(side=TOP,fill=X,padx=5,pady=5)
        domaine = ttk.StringVar(value="")
        self.domaine_entry = ghelp.create_form_entry(self,"Nom domaine : ",domaine)
        self.domaine_entry.insert(0,"www.facebook.com")
        
        ip = ttk.StringVar(value="")
        self.depart_entry = ghelp.create_form_entry(self,"Adresse de depart : ",ip)
        self.depart_entry.insert(0,"192.162.10.3")
        
        self.searchButton = ghelp.create_submit_button(self,"Recherher",self.find_domaine)

    def search_the_short_path(self):
        server_paths = list()
        # recuperer les donnees
        ip1 = self.depart_entry.get()
        domaine = self.domaine_entry.get()
        # la liste des servers a parcourir
        ips = self.dns.get_domaine_ip(domaine)
        # Calculer le path vers chaque destination
        from .application import Application
        server_depart = Application.findServer(ip1)
        for ip in ips:
            server_arrive = Application.findServer(ip)
            server_path = dijkstra.find_short_path(server_depart,server_arrive,Application.servers)
            server_paths.append( server_path )
        
        server_paths = sorted(server_paths,key=lambda x: x.value)

        path = server_paths[0]
        return path
    def find_domaine(self):
        path = self.search_the_short_path()
        from .application import Application
        Application.graphpanel.hilight_on_graph(path,True)
        domaine = self.domaine_entry.get()
        site = path.server_arrivee.get_site(domaine)
        from gui.layout.site import SiteLayout
        SiteLayout(site)