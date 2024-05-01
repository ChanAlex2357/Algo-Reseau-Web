import tkinter as ttk
from tkinter.constants import *
from .controlpanel import ControlPanel
from .graphpanel import GraphPanel
from  .header import Header
from network.dns import Dns
# Declaration des objets a manipuler
dns = Dns()
servers = list()
liaisons = list()
# Configuration de la fenetre
window = ttk.Tk()
window.title("Web Reseau")

# Configuration des differentes composantes de la fenetre 
Header(window)
# La partie qui gere la representation des donnees
GraphPanel(window,dns,servers)
# La partie de l'affichage pour controller les doneess
ControlPanel(window,dns,servers)
window.mainloop()