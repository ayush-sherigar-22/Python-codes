class AddData():
    count=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        AddData.count+=1

    def printname(self):
        print("My name is ",self.name)
        print("My age is",self.age)

obj1=AddData('Ram',20)
obj2=AddData('Om',29)
obj1.printname()
obj2.printname()

print(AddData.count)



# print(obj1.name)
# print(obj1.age)

# print(obj2.name)
# print(obj2.age)

# class AddData():
#     def __init__(self):
#         print("it is constructor.")

#     def demo(self):
#         print("it is a function.")

# obj1=AddData()
# print(obj1.demo())



#there is no need to call a constructor. fucntion sould be called