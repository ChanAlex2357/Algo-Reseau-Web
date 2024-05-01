import tkinter as ttk
from tkinter.constants import *
from .dnspanel import DnsPanel
from .serverspanel import ServersPanel

class ControlPanel(ttk.Frame):
    def __init__(self,window,dns,servers:list=list()):
        super().__init__(master=window,height=300,bg="black")
        self.pack(side=TOP,fill=BOTH,expand=YES)
        DnsPanel(self,dns)
        ServersPanel(self,dns,servers)