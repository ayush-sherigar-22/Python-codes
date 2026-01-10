import math

class circle:
    def __init__(self, radius) :
        self.radius=radius

    def get(self):
        self.radius=int(input("Enter radius :"))

    def area(self):
        area=math.pi*(self.radius)**2
        print("Area is : ", area)

    def perimeter(self):
        perimeter=(2*math.pi*self.radius)
        print("Perimeter is ", perimeter)


cir=circle("0")
cir.get()
cir.area()
cir.perimeter()

