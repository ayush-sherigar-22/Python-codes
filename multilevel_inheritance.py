class Animal:    #base class
    def speak(self):
        print("Animal is speaking. ")

#child class dog inherits the base class Animal

class Dog(Animal): #derived class from Animal. base class for Dog1
    def bark(self):
        print("Dog is barking")

class Dog1(Dog): #derived class from  Dog. 
    def breed(self):
        print("It is a Pug")
d=Dog1()

d.bark()
d.speak()
d.breed()

# d being obj of Dog1 which is derived class(child class) of Dog (parent)  which in turn is a derived class for Animal( grandparent class) can access fucntions and data members of class Animal