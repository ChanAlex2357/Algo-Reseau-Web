import tkinter as ttk
from tkinter.constants import *
from web.site import Site
class SiteLayout(ttk.Frame):
    def __init__(self,site:Site):
        master = ttk.Tk()
        master.title(site.get_nom_domaine())
        super().__init__(master)
        self.site = site
        self.pack(fill=BOTH,expand=YES,padx=20,pady=20)
        content_label = ttk.Label(self,text=site.get_content())
        content_label.pack(expand=YES)