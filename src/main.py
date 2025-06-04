from window import Window
from boids import Boid
import math 


def main():
  
    W, H = 800, 800
    win = Window(W, H)
    c =  win.canvas  
    
    boid = Boid(
        c, x=W/2, y=H/2,
        speed=6,
        heading=math.radians(60),
        size=20,
        color='skyblue'
    )
    
    def on_frame():
        boid.update()
        boid.x %= win.width
        boid.y %= win.height
        
    win.wait_for_close(on_frame=on_frame, delay=50)
    
if __name__=="__main__":
    main() 