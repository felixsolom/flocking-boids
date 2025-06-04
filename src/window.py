from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Boid Simulator")
        
        self.__canvas = Canvas(self.__root, bg="skyblue", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False 
        
    @property
    def canvas(self):
        return self.__canvas 
    
    @property
    def width(self):
        return int(self.__canvas['width'])
    
    @property 
    def height(self):
        return int(self.__canvas['height'])
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def close(self):
        self.__running = False
    
    def wait_for_close(self, on_frame=None, delay=50):
        self.__running = True
        
        def loop():
            if not self.__running:
                print('Window closed')
                return 
            if on_frame:
                on_frame()
            self.redraw()
            self.__root.after(delay, loop)

        loop()
        self.__root.mainloop()

            
    
                