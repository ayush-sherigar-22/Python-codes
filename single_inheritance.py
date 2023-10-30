class Animal:
    def speak(self):
        print("Animal is speaking. ")

#child class dog inherits the base class Animal

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d=Dog()
d.bark()
d.speak()

# d being obj of Dog which is derived class(child class) of Animal (parent) can access fucntions and data members of class Animal