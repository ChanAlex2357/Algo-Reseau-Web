import tkinter as ttk
from tkinter.constants import *
from .dnspanel import DnsPanel
from .serverspanel import ServersPanel
from .serverdetails import ServerDetail
from .recherche import RecherhePanel
class ControlPanel(ttk.Frame):
    def __init__(self,
                 window,
                 dns,
                 servers:list=list(),
                 liaisons:list=list()
        ):
        super().__init__(master=window)
        self.pack(side=LEFT,fill=BOTH,padx=5,pady=5)
        
        self.dns = dns
        self.servers = servers
        self.liaisons = liaisons
        
        self.dns_panel = DnsPanel(self,dns)
        self.servers_panel = ServersPanel(self,dns,servers)
        self.recherhe_panel = RecherhePanel(self)
        self.server_detail_panel = ServerDetail(self)
        