class staffMembers:
    def __init__(self, name,role, id):
        self.name=name
        self.role=role
        self.id=id
    def display(self):
        print("Name of Teacher is ",self.name)
        print("Id of Teacher is ",self.id)
        print("Role of Teacher is ",self.role)

class Professor(staffMembers):
    def __init__(self,subject,name,id):
         self.name=name
         self.role=role
         super().__init__(name,role,id)
         self.subject=subject
         

    def teach(self):
        print("%s teaches %s "%(self.name,self.subject))
  

class AdminStaff(staffMembers):
    def __init__(self,dept,name,id):
     super().__init__(name,role,id)
     self.dept=dept
    def teach(self):
        print("%s is Admin staff  of "%(self.name,self.dept))


class TechnicalStaff(staffMembers):
    def __init__(self,skill,name,id):
     super().__init__(name,role,id)
     self.skill=skill
    def teach(self):
        print("%s is Technical staff  of "%(self.name,self.skill))
 
prof=Professor("Dr.Smith","Prof.",123)
adm=AdminStaff("Mr.Tom","Adm. Staff",567)
tech=TechnicalStaff("Mr.Jim","Tech. Staff",345)

tech.display()