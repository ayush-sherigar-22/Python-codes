list2=int(input("Enter size :"))
list1= input("Enter the list items :").split()




dict={}
for i in range (list2):
    values=input("Enter values :").split()
    dict[list1[i]]=values

print("Created dcitionary is :", dict)

