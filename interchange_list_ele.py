
def swap(list):
    swap1=len(list)
    temp=list[0]
    list[0]=list[swap1-1]
    list[swap1-1]=temp
    return  list

list=input("Enter a list :").split()
print("enter changed list is :",swap(list))