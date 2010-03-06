size(400, 150)
font("HelveticaNeue-Bold", 72)
tp = textpath("Burocrazy", 30, 43)
transform(CORNER)
rotate(random(1, -9))
#drawpath(BezierPath(tp))
tp_points = list(tp.points(100))
from AppKit import NSShadow, NSColor
from nodebox.graphics import Grob
 
class shadow(Grob):
    def __init__(self, x=10, y=10, alpha=0.25, blur=4.0):
        Grob.__init__(self, _ctx)
        self._shadow = NSShadow.alloc().init()
        self._shadow.setShadowOffset_((x, -y))
        self._shadow.setShadowColor_(color(0, 0, 0, alpha)._rgb)
        self._shadow.setShadowBlurRadius_(blur)
        self.draw()
    def _draw(self):
        self._shadow.set()
        
shadow(blur=5.0, x=2.0, y=2.0)

def shard(x=None, y=None):
    if x is None:
        x = random(WIDTH)
    if y is None:
        y = random(HEIGHT)
    beginpath(x, y)
    lineto(x + random(-dx, dx), y + random(-dy, dy))
    lineto(x + random(-dx, dx), y + random(-dy, dy))
    return endpath(draw=False)
    
dx = dy = 10.0
for i in range(30):
    pt = choice(tp_points)
    tp = tp.union(shard(pt.x, pt.y), flatness=0.1)

dx = dy = 30.0
for i in range(60):
    #shape = star(random(WIDTH), random(HEIGHT), 3, 3, 5, draw=False)
    tp = tp.difference(shard(), flatness=0.1)
fill(0.2, 0.0, 0.1)
drawpath(tp)