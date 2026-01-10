class dept:
    
    def __init__(self, dept_id, name):
        self.dept_id=dept_id
        self.name=name


    def getdata(self):
        print("Accepting data :")
        self.name=input("Enter name: ")
        self.dept_id=int(input("Enter id :"))


    def data(self):
        print("Dept name is ",self.name," and dept id is ", self.dept_id )


        

dep=dept("blank",0)

dep.getdata()
dep.data()