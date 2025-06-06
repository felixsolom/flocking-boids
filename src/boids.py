import math
import colorsys

class Boid: 
    def __init__ (self, canvas, x, y,
                  speed=4, heading=0,
                  size=15, color='grey'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = speed
        self.prev_speed = speed
        self.heading = heading
        self.size = size
        self.color = color 
        self.id = None 
        self.cruise_speed = 3.0
        self.max_accel = 0.2
        self.max_speed = 9.0
        self.min_speed = 0.5
        self.last_turn = 0.0
         
        
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
            self.canvas.itemconfig(self.id, fill=self.color)
            
    @staticmethod
    def accel_to_color(accel, min_a=-1, max_a=1):
        t = max(0.0, min(1.0, (accel - min_a) / (max_a - min_a)))
        hue = (1 - t) * 240 / 360 
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        return '#{0:02x}{1:02x}{2:02x}'.format(int(r*255), int(g*255), int(b*255))
            
    def update(self):
        desired_change = (self.cruise_speed - self.speed) * 0.4
        thrust = max(-self.max_accel, min(self.max_accel, desired_change))
        turn_factor = min(abs(self.last_turn) / self.max_accel, 1.0)
        brake = turn_factor * self.max_accel * 1.5
        accel = thrust - brake 
        accel = max(-self.max_accel, min(self.max_accel, accel))
        self.speed += accel 
        self.speed = max(self.min_speed, min(self.max_speed, self.speed))
        self.x += math.cos(self.heading) * self.speed
        self.y += math.sin(self.heading) * self.speed
        
        self.color = Boid.accel_to_color(accel, min_a=-self.max_accel, max_a=self.max_accel)
        self.draw()
        
    