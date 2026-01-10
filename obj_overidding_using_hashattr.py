class Principal:
    def role(self):
        print("I'm managing all activity of college. ")

class Dean:
    def order(self):
        print("I'm taking all the decisions. ")


def  call(obj):
    if hasattr(obj, 'role'):
        obj.role()
    else:
        obj.order()

obj=Principal()
call(obj)

obj=Dean()
call(obj)