from network import server
from gui.layout import GraphLayout

class ServerLayout(GraphLayout):
    SERVER_WIDTH = 50
    SERVER_HEIGHT = 60
    def __init__(self,graphpanel,server,x,y):
        self.canevas = graphpanel.canevas
        
        # Creation d'un rectangle representant le server
        geom = self.canevas.create_rectangle(
            x,
            y,
            x+ServerLayout.SERVER_WIDTH,
            y+ServerLayout.SERVER_HEIGHT,
            fill="cyan"
        )
        self.float_text = self.canevas.create_text(
            x+ServerLayout.SERVER_WIDTH/2,y-10,text=server.get_adresse_ip(),
            fill="black",
            font=("Helvetica",12)
        )
        super().__init__(server,geom)
        self.move_events()
    def set_server(self,server):
        self.object = server
    def get_server(self):
        return self.object
    
    def move_events(self):
        self.canevas.tag_bind(self.geometrie,"<ButtonPress-1>",self.on_press)
        self.canevas.tag_bind(self.geometrie,"<B1-Motion>",self.moving)
        
    def on_press(self,event):
        self.last_x = event.x
        self.last_y = event.y
    ''' Deplacer la representation graphique du server '''
    def moving(self,event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        self.canevas.move(self.geometrie,dx,dy)
        self.canevas.move(self.float_text,dx,dy)
        self.on_press(event)