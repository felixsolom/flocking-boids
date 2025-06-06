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
        self.max_speed = 9.0
        
        
    def update(self):
        for boid in self.boids:
            neighbors = [other for other in self.boids
                        if other is not boid and 
                        self._distance(boid, other) < self.perception]
            
            steer_sep = self._separation(boid, neighbors)
            steer_ali = self._alignment(boid, neighbors)
            steer_coh = self._cohesion(boid, neighbors)
            
            turn = steer_sep * 1.5 + steer_ali * 1.0 + steer_coh * 1.0
            boid.last_turn = turn 
            boid.heading += turn 
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
    
    def _alignment(self, boid, neighbors):
        avg_dx = avg_dy = 0
        for other in neighbors:
            avg_dx += math.cos(other.heading)
            avg_dy += math.sin(other.heading)
        count = len(neighbors)
        if count:
            avg_dx /= count
            avg_dy /= count 
            angle =  math.atan2(avg_dy, avg_dx)
            return self._steer_angle(boid, angle)
        return 0
    
    def _cohesion(self, boid, neighbors):
        center_x = center_y = 0
        for other in neighbors:
            center_x += other.x
            center_y += other.y
        count = len(neighbors)
        if count:
            center_x /= count
            center_y /= count
            angle = math.atan2(center_y - boid.y, center_x - boid.x)
            return self._steer_angle(boid, angle)
        return 0
    
    def _steer_angle(self, boid, target_angle):
        diff = (target_angle - boid.heading + math.pi) % (2*math.pi) - math.pi
        return max(-self.max_force, min(self.max_force, diff))
    
    def _wrap_edges(self, boid):
        if boid.x < 0: boid.x = self.width
        if boid.x > self.width: boid.x = 0
        if boid.y < 0: boid.y = self.height
        if boid.y > self.height: boid.y = 0 
        
        

            