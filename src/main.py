from window import Window
from flock import Flock
from obstacles import Obstacle
import random


def main():
  
    W, H = 1600, 1200
    win = Window(W, H)
    obstacles = []
    
    def toggle_obstacle(event):
        for obs in obstacles:
            if obs.contains(event.x, event.y):
                obs.remove()
                obstacles.remove(obs)
                return 
        r = random.randint(20, 60)
        obstacles.append(Obstacle(win.canvas, event.x, event.y, r))
            
    win.canvas.bind("<Button-1>", toggle_obstacle)
                 

    flock = Flock(win.canvas, win.width, win.height, num_boids=200, obstacles=obstacles)  
    

    def on_frame():
        flock.update()
        
        
        
    win.wait_for_close(on_frame=on_frame, delay=30)
    
if __name__=="__main__":
    main() 