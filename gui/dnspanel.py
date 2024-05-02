import tkinter as ttk
from tkinter.constants import *
class DnsPanel(ttk.Frame):
    def __init__(self,master,dns):
        super().__init__(master,width=500)
        self.pack(side=TOP,fill=Y,padx=5,pady=10)
        self.master = master
        self.dns = dns
        # Creation de l'en tete DNS
        self.header = self.create_header()
    
    def create_header(self):
        header = ttk.Frame(self)
        header.pack(side=TOP,fill=BOTH,expand=YES)
        self.create_title(header)
        return header
        
    def create_title(self,header):
        label =  ttk.Label(header,text="DNS",)
        label.pack(fill=BOTH,expand=YES)