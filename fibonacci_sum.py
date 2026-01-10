def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

list=[]
ans=0
n=int(input("Enter a number :"))
for i in range(0,n):
    list.append((fibo(i)))
print(list)

for i in range(len(list)):
    ans+=list[i]
print(ans) 