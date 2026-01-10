from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):
      print("parent class.")

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")

class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")


 
t=Triangle()
t.noofsides()
t.sides()
p=Pentagon()
p.noofsides()

q=Quadrilateral()
q.noofsides()