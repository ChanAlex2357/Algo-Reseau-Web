from network.server import Server
from gui.layout import GraphLayout
import tkinter as ttk

class ServerLayout(GraphLayout):
    SERVER_WIDTH = 50
    SERVER_HEIGHT = 60
    def __init__(self,graphpanel,server:Server,x,y):
        self.canevas = graphpanel.canevas
        self.graphpanel = graphpanel
        # Creation d'un rectangle representant le server
        geom = self.set_layout_id(server,x,y)
        
        super().__init__(
            server,
            self.canevas,
            geom,
            x,
            y,
            ServerLayout.SERVER_WIDTH,
            ServerLayout.SERVER_HEIGHT
        )
        self.move_events()

    def set_layout_id(self,server,x,y):
        color = "cyan";
        if not server.get_etat:
            color = "gray"
        geom = self.canevas.create_rectangle(
            x,
            y,
            x+ServerLayout.SERVER_WIDTH,
            y+ServerLayout.SERVER_HEIGHT,
            fill="cyan",
            outline="",
            width = 2
        )
        self.float_text = self.canevas.create_text(
            x+ServerLayout.SERVER_WIDTH/2,y+10,text=server.get_adresse_ip(),
            fill="black",
            font=("Helvetica",10)
        )
        return geom
    def set_server(self,server):
        self.object = server
    def get_server(self):
        return self.object
    
    def move_events(self):
        self.canevas.tag_bind(self.geometrie,"<ButtonPress-1>",self.on_press)
        self.canevas.tag_bind(self.geometrie,"<B1-Motion>",self.moving)
        self.canevas.tag_bind(self.geometrie,"<Button-3>",self.pop_menu)
        
    def on_press(self,event):
        self.last_x = event.x
        self.last_y = event.y
        from gui.application import Application
        Application.controlpanel.server_detail_panel.update_content(self.get_server())
        
    ''' Deplacer la representation graphique du server '''
    def moving(self,event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        self.canevas.move(self.geometrie,dx,dy)
        self.canevas.move(self.float_text,dx,dy)
        self.move(dx,dy)
        self.move_liaisons()
        self.on_press(event)

    ''' Afficher le Menu de choix lors d'un clic droit
        Args
            Les donnees de l'evenement
    '''
    def pop_menu(self,event):
        x = event.x_root
        y = event.y_root
        from gui.application import Application
        Application.graphpanel.pop_server_menu(x,y,self.get_server())
        
    def move_liaisons(self):
        for liaison in self.get_server().get_lisaisons():
            try :
                layout  = liaison.get_layout()
                layout.move()
            except Exception:
                pass
            
    def hilight(self,color="black"):
        self.canevas.itemconfig(self.geometrie,outline=color)
    def unhilight(self):
        self.canevas.itemconfig(self.geometrie,outline="")

    def remove_layout(self):
        super().remove_layout()
        self.canevas.delete(self.float_text)