class Principal:
    def role(self):
        print("I'm managing all activity of college. ")

class Dean:
    def role(self):
        print("I'm taking all the decisions. ")

class Hod:
    def role(self):
        print("I have responsibility of teachers and faculty. ")

class Faculty:
    def role(self):
        print("I have to teach class. ")

def  func(obj):
    obj.role()

campus=[Principal(),Dean(),Faculty(),Hod()]
for obj in campus:     #obj=[0:Principal(),1:Dean(),2:Faculty(),3:Hod()]
    # obj=[0 : Principal(), 1:Dean(), 2:Hod()]
    func(obj)
