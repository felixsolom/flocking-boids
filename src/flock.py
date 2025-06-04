import math
import random
from boids import Boid

class Flock:
    def __init__(self, canvas, width, height, num_boids=30):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.boids = []
        for _ in range(num_boids):
            x = random.uniform(0, width)
            y = random.uniform(0, height)
            heading = random.uniform(0, 2*math.pi)
            self.boids.append(Boid(canvas, x, y, heading=heading))
        self.perception = 50
        self.max_force = 0.1
        self.max_speed = 5
        
    def update(self):
        for boid in self.boids:
            neighbors = [other for other in self.boids
                        if other is not boid and 
                        self._distance(boid, other) < self.perception]
            
        steer_sep = self._separation(boid, neighbors)
        steer_ali = self._alighnment(boid, neighbors)
        steer_coh = self._cohision(boid, neighbors)
        
        boid.heading += steer_sep * 1.5 + steer_ali * 1.0 + steer_coh * 1.0
        boid.speed = min(boid.speed, self.max_speed)
        self._wrap_edges(boid)
        boid.update()
        
    def _distance(self, b1, b2):
        return math.hypot(b1.x - b2.x, b1.y - b2.y)
    
    def _separation(self, boid, neighbors):
        steer_x = steer_y = 0
        for other in neighbors:
            dx = boid.x - other.x
            dy = boid.y - other.y
            dist = math.hypot(dx, dy)
            if dist > 0:
                steer_x += dx / dist
                steer_y += dy / dist
        count = len(neighbors)
        if count:
            steer_x /= count
            steer_y /= count 
            angle = math.atan2(steer_y, steer_x)
            return self._steer_angle(boid, angle)
        return 0 
            