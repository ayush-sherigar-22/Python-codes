
class dept:
    
    def __init__(self, dept_id, name):
        self.dept_id=dept_id
        self.name=name


    def getdata(self):
        print("Accepting data :")
        self.name=input("Enter dept name: ")
        self.dept_id=int(input("Enter dept id :"))


    def data(self):
        print("Dept name is ",self.name," and dept id is ", self.dept_id )

class faculty(dept):
    def __init__(self, name1):
        self.name=name1

    def staff(self):
        self.name1=input("Enter your name :")
        print("Name of staff is ", self.name1)
        


staff=faculty("John")
staff.staff()
staff.getdata()
staff.data()