import tkinter as ttk
from tkinter.constants import *
import gui.helpers as ghelp 
class Header(ttk.Frame):
    def __init__(self,window):
        super().__init__(window,padx=50)
        self.pack(side=TOP,fill=X)
        
        domaine = ttk.StringVar(value="")
        self.domaine_entry = ghelp.create_form_entry(self,"Nom domaine : ",domaine)
        
        ip = ttk.StringVar(value="")
        self.depart_entry = ghelp.create_form_entry(self,"Adresse de depart : ",ip)
        
        self.searchButton = ghelp.create_submit_button(self,"Recherher",)