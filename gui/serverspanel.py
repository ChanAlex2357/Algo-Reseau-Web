import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from network.server import Server

class ServersPanel(tk.Frame):
    def __init__(self,window,dns,servers:list=list()):
        super().__init__(window)
        self.pack(side=TOP,fill=BOTH,padx=5,pady=5)
        self.window = window
        self.servers = servers
        self.dns = dns
        # Creation de l'entete 'Servers'
        self.header = self.create_header()
        # Creation du tableau des servers a partir de la liste des servers
        self.serverTab = self.create_servers_tree()
        # Rafrachir le contenu du  tableau
        self.refresh_servers_tab()
    
    def create_header(self):
        header = ttk.Frame(self)
        header.pack(side=TOP,fill=X)
        self.create_title(header)
        return header
        
    def create_title(self,header):
        label =  ttk.Label(header,text="Servers")
        label.pack()
    
    '''Creation d'un tableau qui liste les servers crees'''
    def create_servers_tree(self):
        frame = ttk.Frame(self)
        frame.pack()
        serverTab = ttk.Treeview(frame,columns=("Server Name","Adresse IP"),show="headings")
        serverTab.heading("Server Name",text="Server Name")
        serverTab.heading("Adresse IP",text="Adresse IP")
        serverTab.pack(side=LEFT,padx=5,pady=5)

        return serverTab

    '''Insertion d'un nouveau server dans le tableau'''
    def add_server(self,server):
        self.serverTab.insert(
            "","end",
            values=(
                server.get_nom_server(),
                server.get_adresse_ip()
            ))
    '''Rafraichi la liste des donnees dans le tableau'''
    def refresh_servers_tab(self):
        for item in self.serverTab.get_children():
            self.serverTab.delete(item)
        for server in self.servers:
            self.add_server(server)