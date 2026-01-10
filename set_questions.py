def max_min(set):
    print(max(set))
    print(min(set))


def one_common(a,b):

 
    print("Common Elements are :",a.intersection(b))

def missing__addtional_element(a,b):
    set1=a.difference(b)
    set2=b.difference(a)
    print("missing values in set :",set2)
    print("additional values in set :",set1)


def binary(a):
    p=set(num)
    
    s={'0','1'}

    if s==p or p=={"0"} or p=={"1"}:
        print("Its Binary .")

    else:
        print("Its NOT Binary.")



set3={8, 16, 24, 1, 25, 3, 10, 65, 55}

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}


list1 = {1, 2, 3, 4, 5, 6}
list2 = {4, 5, 6, 7, 8}
max_min(set3)
one_common(a,b)
missing__addtional_element(list1,list2)
missing__addtional_element(list2, list1)

num="01010101010"

binary(num)