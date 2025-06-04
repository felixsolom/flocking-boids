from window import Window
from flock import Flock


def main():
  
    W, H = 800, 800
    win = Window(W, H)
    flock = Flock(win.canvas, win.width, win.height, num_boids=50)  
    
    '''
    boid = Boid(
        c, x=W/2, y=H/2,
        speed=6,
        heading=math.radians(60),
        size=20,
        color='skyblue'
    )
    '''
    
    def on_frame():
        flock.update()
        
        
    win.wait_for_close(on_frame=on_frame, delay=30)
    
if __name__=="__main__":
    main() 