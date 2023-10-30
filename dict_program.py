class_data={}
print("Enter the class data: \n")
roll=int(input("Enter roll no : "))
name=input(" \n Enter name :")
class_data[roll]=name
print(class_data)

while(1):

    choice=input("Do you want to enter more data (Y/N) : ")
    if choice in {"n","N"}:
        
                 print(class_data)
                 break
           
    elif choice in {"Y","y"}:
        roll=int(input("\n Enter roll no : "))
        name=input(" \n Enter name :")
        class_data[roll]=name
        print(class_data)