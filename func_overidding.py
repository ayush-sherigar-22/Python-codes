class Animal:    #base class
    def speak(self):
        pass

#child class dog inherits the base class Animal

class Dog(Animal): #derived class from Animal. base class for Dog1
    def speak(self):
        print("Dog is speaking")

class Dog1(Animal): #derived class from  Dog. 
    def speak(self):
        print("It is a Pug")

dog=Dog()
doggo=Dog1()


dog.speak()
doggo.speak()

# d being obj of Dog1 which is derived class(child class) of Dog (parent)  which in turn is a derived class for Animal( grandparent class) can access fucntions and data members of class Animal