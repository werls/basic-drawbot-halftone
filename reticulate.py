from drawBot import *

class reticulate():

    def __init__(self,path,resolution = 100,dotSize = 20):
        self.path = path
        self.resolution = resolution
        self.dotSize = dotSize
        self.w,self.h = imageSize(self.path)
        
        self.draw()

    def draw(self):
        newPage(self.w,self.h)
        fill(1)
        rect(0,0,self.w,self.h)
        
        translate(-self.dotSize/2,-self.dotSize/2)

        if self.w > self.h:
            ponto = self.w/self.resolution + 1
        else:
            ponto = self.h/self.resolution + 1    
        # ponto = self.dotSize
        
        for width in range(self.resolution):
            x = ponto+width*ponto
            for height in range(self.resolution):
                y = ponto+height*ponto
                
                color = imagePixelColor(self.path,(x,y))
                if color:
                    r,g,b,a = color
                    if r or g or b or a != 0:
                        fill(r,g,b,a)
                        oval(x,y,self.dotSize,self.dotSize)