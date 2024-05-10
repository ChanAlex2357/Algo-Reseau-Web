import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from network.server import Server
from gui.formulaire.liaison import LiaisonFormulaire
from gui.formulaire.site import SiteFormulaire

class ServerDetail(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack(side=TOP,fill=BOTH,padx=5,pady=5)
        self.header = self.create_header()
        self.create_button_frame()
        self.content = self.create_content()
        self.server_detailed = None
        

    def create_button_frame(self):
        frame = ttk.Frame(self)
        frame.pack(side=TOP,expand=YES,fill=BOTH)
        # Boutton d'ajout de site dans le server
        self.add_site_btn = ttk.Button(frame,text="ajouter site",command=self.add_site)
        self.add_site_btn.pack(side=LEFT)
        # Boutton d'ajout de liaison sur le server
        self.add_liaison_btn = ttk.Button(frame,text="ajouter liaison",command=self.add_liaison)
        self.add_liaison_btn.pack(side=LEFT)

    def add_site(self):
        master = tk.Tk()
        master.title("Formulaire site")
        from gui.application import Application 
        SiteFormulaire(master, Application.graphpanel , self.server_detailed)
        
        
    def add_liaison(self):
        master = tk.Tk()
        master.title("Formulaire liaison")
        from gui.application import Application 
        LiaisonFormulaire(master, Application.graphpanel , self.server_detailed)
    
    def update_content(self,server):
        self.release_content()
        self.server_detailed = server
        self.content.configure(text= server.stringify())
        
    def release_content(self):
        # if self.server_detailed is not None:
        #     self.server_detailed.get_layout().unhilight()
        self.server_detailed = None

    def create_content(self):
        content = ttk.Label(self,text="Server detail content")
        content.pack(fill=BOTH,side=LEFT,expand=YES)
        return content

    def create_header(self):
        header = ttk.Frame(self)
        header.pack(side=TOP,fill=X)
        self.create_title(header)
        return header

    def create_title(self,header):
        label =  ttk.Label(header,text="Server Detail")
        label.pack()