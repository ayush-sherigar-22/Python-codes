tuple1=(1,2,3,1997,2002,'sherigar',9,88,"ayush")
tuple2=('cs','ab',"o")
print("tuple 1 element at 0 index is",tuple1[0])
print("tuple 2 after slice",tuple2[0:3])
tuple3=tuple1+tuple2
print("tuple3 is",tuple3)
print("length of tuple 1 is",len(tuple1))
print("length of tuple 2 is",len(tuple2))
print("max of tuple 2 is",max(tuple2))
print("min of tuple 1 is",min(tuple2))
list1=[1,2,3,1997,2002,0,9,88,766543]
tup=tuple(list1)
print("tup from lis1 is",tup)