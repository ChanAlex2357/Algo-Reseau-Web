import tkinter as tk
from tkinter.constants import *
class DnsPanel(tk.Frame):
    def __init__(self,master,dns):
        super().__init__(master,)
        self.pack(side=RIGHT,expand=YES,fill=BOTH,padx=5,pady=10)
        self.master = master
        self.dns = dns