import matplotlib.pyplot as plt
import matplotlib
import oop.Circle
import oop.Point
import oop.Rectangle

def test_internal_axes():
    fig,axes = plt.subplots(figsize=(10,10))
    a = oop.Point.Point(2,2,axes)
    axes = a.draw()
    b = oop.Circle.Circle(4,4,2,axes)
    b.draw()
    plt.show()
    
def test_external_axes():
    a = oop.Point.Point(2,2)
    axes = a.draw()
    b = oop.Circle.Circle(4,4,2,axes)
    axes = b.draw()
    
    c = oop.Point.Point(2,2)
    axes = c.draw()
    d = oop.Rectangle.Rectangle(4,4,2,2,axes)
    axes = d.draw()
    
    plt.show()
      
if __name__ == "__main__":
    print(matplotlib.__version__)
    test_external_axes()
