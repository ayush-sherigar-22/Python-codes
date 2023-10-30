class_data={}
print("Enter the class data: \n")
roll=int(input("Enter roll no : "))
name=input(" \n Enter name :")
class_data[roll]=name
print(class_data)

while(1):

    choice=input("Do you want to enter more data (Y/N) : ")
    if choice in {"n","N"}:
        class_keys=list(class_data.keys())
        class_keys.sort()
        sorted_data={i:class_data[i] for i in class_keys}
        print("\n",sorted_data,"\n")
        break
    elif choice in {"Y","y"}:
        roll=int(input("\n Enter roll no : "))
        name=input(" \n Enter name :")
        class_data[roll]=name
        