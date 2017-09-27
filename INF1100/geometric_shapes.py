#7.4
class Rectangle:
    def __init__(self,x0,y0,W,H):
        self.x0, self.y0, self.W, self.H = x0, y0, W, H

    def area(self):
        return self.W*self.H

    def perimeter(self):
        return 2*self.H+2*self.W

r=Rectangle(1,1,3,2)
print 'A rectangle with height %g and width %g at (%g, %g) has area %g' % \
       (r.H, r.W, r.x0, r.y0, r.area())

def test_Rectangle():
    W=3;H=2
    r=Rectangle(1,1,W,H)
    exact_area=6
    exact_perimeter=10
    tol=1e-14
    diff_area=abs(r.area()-exact_area)
    diff_perimeter=abs(r.perimeter()-exact_perimeter)
    assert diff_area < tol, 'bug in Rectangle.area, diff=%s'%diff_area
    assert diff_perimeter < tol, 'bug in Rectangle.perimeter, diff=%s'%diff_perimeter
test=test_Rectangle()

class Triangle:
    def __init__(self,x0,y0,x1,y1,x2,y2):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2

    def area(self):
        a=self.x0*(self.y1-self.y2)
        b=self.x1*(self.y2-self.y0)
        c=self.x2*(self.y0-self.y1)
        return abs(a+b+c)/2.

    def perimeter(self):
        from math import sqrt
        len01=sqrt((self.x1-self.x0)**2+(self.y1-self.y0)**2)
        len02=sqrt((self.x2-self.x0)**2+(self.y2-self.y0)**2)
        len12=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        return len01+len02+len12

t=Triangle(0,0,1,0,1,2)
print 'A triangle with vertices at (%g, %g), (%g, %g), (%g, %g) has area %g' % \
       (t.x0, t.y0, t.x1, t.y1, t.x2, t.y2, t.area())

def test_Triangle():
    x0=0;y0=0;x1=1;y1=0;x2=1;y2=2
    r=Triangle(x0,y0,x1,y1,x2,y2)
    exact_area=1
    exact_perimeter=1+2+5**0.5
    tol=1e-14
    diff_area=abs(t.area()-exact_area)
    diff_perimeter=abs(t.perimeter()-exact_perimeter)
    assert diff_area < tol, 'bug in Triangle.area, diff=%s'%diff_area
    assert diff_perimeter < tol, 'bug in Triangle.perimeter, diff=%s'%diff_perimeter
test=test_Triangle()
