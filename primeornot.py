num=int(input("Enter a number :"))
flag=True
if num>1:
    for i in range(2,int(num/2)):
        if(num % i ==0):
            print(str(num)+" is not prime.")
            flag=False
            break

if flag:
    print(str(num)+ " is prime.")
