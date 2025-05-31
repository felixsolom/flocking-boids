import math

class Boid: 
    def __init__ (self, canvas, x, y,
                  speed=4, heading=0,
                  size=15, color='grey'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading
        self.size = size
        self.color = color 
        self.id = None 
        
    def _triangle_points(self):
        tx = self.x + math.cos(self.heading) * self.size
        ty = self.y + math.sin(self.heading) * self.size
        back = self.heading + math.pi
        left = (
            self.x + math.cos(back + math.pi/6) * self.size*0.6,
            self.y + math.sin(back + math.pi/6) * self.size*0.6
        )
        right = (
            self.x + math.cos(back - math.pi/6) * self.size*0.6,
            self.y + math.sin(back - math.pi/6) * self.size*0.6
        )
        return [tx, ty, left[0], left[1], right[0], right[1]]
    
    def draw(self):
        pts = self._triangle_points()
        if self.id is None:
            self.id = self.canvas.create_polygon(
                pts, fill=self.color, outline='black'
            )
        else:
            self.canvas.coords(self.id, *pts)
            
    def update(self):
        self.x += math.cos(self.heading) * self.speed
        self.y += math.sin(self.heading) * self.speed
        self.draw()