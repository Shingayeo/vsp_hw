import matplotlib.pyplot as plt
import matplotlib.patches
from .Point import Point

class Rectangle(Point):
    
    def __init__(self, x, y, w, h, _axes=None):
        super().__init__(x,y,_axes)
        self.w = w
        self.h = h
        
    def draw(self):
        super().draw()
        r = matplotlib.patches.Rectangle(
            xy = (self.x, self.y),
            width = self.w,
            height = self.h,
            fc = 'purple',
            ec = 'blue',
        )
        self.axes.add_patch(r)
        return self.axes

if __name__ == "__main__":
    a = Rectangle(3,3,1,1)
    a.draw()
    a.show()