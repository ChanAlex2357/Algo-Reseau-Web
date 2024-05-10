from tkinter import ttk
from tkinter.constants import *
from web.site import Site
class DnsPanel(ttk.Frame):
    def __init__(self,master,dns):
        super().__init__(master,width=500)
        self.pack(side=TOP,fill=Y,padx=5,pady=10)
        self.master = master
        self.dns = dns
        # Creation de l'en tete DNS
        self.header = self.create_header()
        # Creation d'un tableau des sites enregister
        self.siteTab =  self.create_site_tree()
        # Rafrachir le contenu avec les donnees actuels
        self.refresh_sites_tab()
        
    
    def create_header(self):
        header = ttk.Frame(self)
        header.pack(side=TOP,fill=BOTH,expand=YES)
        self.create_title(header)
        return header
        
    def create_title(self,header):
        label =  ttk.Label(header,text="DNS",)
        label.pack(fill=BOTH,expand=YES)
        
        
    '''Creation d'un tableau qui liste les sites cree'''
    def create_site_tree(self):
        frame = ttk.Frame(self)
        frame.pack()
        siteTab = ttk.Treeview(frame,columns=("Nom"),show="headings")
        siteTab.heading("Nom",text="Nom domaines")
        siteTab.pack(side=LEFT,padx=5,pady=5)
        return siteTab

    '''Insertion d'un nouveau site dans le tableau'''
    def add_site(self,site:str):
        self.siteTab.insert(
            "","end",
            values=(
                site
            ))

    '''Rafraichi la liste des donnees dans le tableau'''
    def refresh_sites_tab(self):
        for item in self.siteTab.get_children():
            self.siteTab.delete(item)
        for site in self.dns.get_sites().keys():
            self.add_site(site)