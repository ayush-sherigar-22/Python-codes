list1=[1,2,3,1997,2002,0,9,88,766543]
list2=[1,2,3,4,5,6,7]
print("the member at list[0]:",list1[0])
list1[0]=2000
print("the updated member at list[0]:",list1[0])
del list1[0]
print("the updated member at list:",list1)
print("sliced list2 is :",list2[0:3])
list3=["phy",'chem','maths','bio']
print("length of list 3 is:",len(list3))
list4=len(range(3))
print("list 4 is",list4)
tuple=(123,"msd",7,2007,2011,"mahi")
lst=list(tuple)
print("tuple to list is:",lst)
list1.append(99999999)
print("appended list is ",list1)
list1.extend(list2)
print("extended list is:",list1)
list1.pop(1)
print("popped list is",list1)
list1.remove(88)
print("after deleting list is :",list1)
list1.reverse()
print("after rev list is :",list1)
list1.sort()
print("after sorting list is :",list1)
print("max of  list is :",max(list1))
l1=["ab",'df','kjj']
print("min of  l1 is :",min(l1))
list1.insert(1,'a23')
print("updated list is",list1)
