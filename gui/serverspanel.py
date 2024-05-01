import tkinter as ttk
from tkinter.constants import *

class ServersPanel(ttk.Frame):
    def __init__(self,window,dns,servers:list=list()):
        super().__init__(window,)
        self.pack(side=LEFT,expand=YES,fill=BOTH,padx=5,pady=10)
        self.window = window
        self.servers = servers
        self.dns = dns