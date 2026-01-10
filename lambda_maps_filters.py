def square(x):
    return x**2
print (square(4))

n=int(input("Enter a number :"))

result=(lambda x: x**2)(n)
print(result)
 

# map

def add(x):
    return x*2

results=[10, 20, 30 , 40, 50]

ans=list(map(add,results))
print(ans)


#using map and lambda

ans=list(map(lambda x: x*3, results))
print(ans)

#filters
num=[1,2,3,4,5,6,7,8,9,10,110]
result= list(filter(lambda x:x%2==0, num))
print(result)