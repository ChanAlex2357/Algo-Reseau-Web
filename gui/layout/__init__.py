class GraphLayout():
    def __init__(self,obj,canevas,geometrie,x,y,width,height):
        self.object  = obj
        self.geometrie = geometrie
        self.canevas = canevas
        
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        
    def get_width(self):
        return self.width
    def set_width(self,width):
        self.width = width
    def get_height(self):
        return self.height
    def set_height(self,height):
        self.height = height
    
    def set_location(self,x,y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self,x):
        self.x = x
    def get_x(self):
        return self.canevas.coords(self.geometrie)[0]
    def get_center_x(self):
        x1,y1,x2,y2 = self.canevas.coords(self.geometrie)
        return (x2+x1)/2
    
    def set_y(self,y):
        self.y = y
    def get_center_y(self):
        x1,y1,x2,y2 = self.canevas.coords(self.geometrie)
        return (y2+y1)/2
    def get_y(self):
        return self.canevas.coords(self.geometrie)[1]
    
    def move(self,dx,dy):
        newx = self.get_x() + dx
        newy = self.get_y() + dy
        self.set_location(newx,newy)
    def remove_layout(self):
        self.canevas.delete(self.geometrie)
    
        