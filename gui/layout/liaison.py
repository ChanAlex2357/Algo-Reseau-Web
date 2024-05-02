from network.liaison import Liaison
from gui.layout import GraphLayout
class CircleValue():
    CIRCLE_RADIUS = 10
    def __init__(self,line,canevas,rayon,value):
        self.canevas = canevas
        self.line = line
        self.x = line.get_center_x()
        self.y = line.get_center_y()
        self.rayon = rayon
        self.value = value
        self.circle = canevas.create_oval(
            self.x - rayon , self.y - rayon,
            self.x + rayon , self.y + rayon,
            fill="white"
        )
        self.textvalue = canevas.create_text(
            self.x,
            self.y,
            text=f"{value}",
            fill="black",
            font=("Helvetica",10)
        )
    def get_circle(self):
        return self.circle
    def get_text_value(self):
        return self.textvalue
    def move(self):
        canevas = self.canevas 
        line = self.line
        rayon  = self.rayon
        self.x = line.get_center_x()
        self.y = line.get_center_y()

        x1 = self.x - rayon
        y1 = self.y - rayon
        x2 = self.x + rayon
        y2 = self.y + rayon
        
        canevas.coords(self.circle,x1,y1,x2,y2)
        canevas.coords(self.textvalue,self.x,self.y)

class LiaisonLayout(GraphLayout):
    def __init__(self,graphpanel,liaison:Liaison):
        self.canevas = graphpanel.canevas
        # Creation d'un rectangle representant le server
        x1 = liaison.get_servers()[0].get_layout().get_center_x()
        y1 = liaison.get_servers()[0].get_layout().get_center_y()
        x2 = liaison.get_servers()[1].get_layout().get_center_x()
        y2 = liaison.get_servers()[1].get_layout().get_center_y()
        geom = self.canevas.create_line(
            x1,y1,x2,y2,
            fill="black",
            width=2
        )
        self.canevas.tag_lower(geom)
        super().__init__(
            liaison,
            self.canevas,
            geom,
            x1,y1,x2-x1,y2-y1
        )
        self.circle_value = CircleValue(
            self,
            self.canevas,
            CircleValue.CIRCLE_RADIUS,
            liaison.get_temps_reponse()
        )

    def set_liaison(self,liaison):
        self.object = liaison
    def get_liaison(self):
        return self.object

    def move(self):
        liaison = self.get_liaison()
        canevas = self.canevas
        self.hilight();
        x1 = liaison.get_servers()[0].get_layout().get_center_x()
        y1 = liaison.get_servers()[0].get_layout().get_center_y()
        x2 = liaison.get_servers()[1].get_layout().get_center_x()
        y2 = liaison.get_servers()[1].get_layout().get_center_y()
        self.canevas.coords(self.geometrie,x1,y1,x2,y2)
        self.circle_value.move()
    def hilight(self,color="red"):
        self.canevas.itemconfig(self.geometrie,fill=color)
    def unhilight(self):
        self.canevas.itemconfig(self.geometrie,fill="black")