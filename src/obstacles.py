import  math

class Obstacle:
    def __init__(self, canvas, x, y, radius):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.id = canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill='red', outline=''
        )
        
    def contains(self, px, py):
        return math.hypot(self.x - px, self.y - py) <= self.radius
    
    def remove(self):
        self.canvas.delete(self.id)
    