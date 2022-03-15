from drawBot import *

class reticulate():
    def __init__(self ,path, resolution = 100, dot_size = 20):
        self.path = path
        self.resolution = resolution
        self.dot_size = dot_size
        self.w, self.h = imageSize(self.path)
        self.draw()

    def draw(self):
        newPage(self.w, self.h)
        fill(1)
        rect(0, 0, self.w, self.h)
        
        translate(-self.dot_size / 2, -self.dot_size / 2)

        if self.w > self.h:
            dot = self.w / self.resolution + 1
        else:
            dot = self.h / self.resolution + 1    
        # dot = self.dot_size
        
        for width in range(self.resolution):
            x = dot + width * dot
            for height in range(self.resolution):
                y = dot + height * dot        
                color = imagePixelColor(self.path, (x, y))
                if color:
                    r, g, b, a = color
                    if r or g or b or a != 0:
                        fill(r,g,b,a)
                        oval(x,y,self.dot_size,self.dot_size)