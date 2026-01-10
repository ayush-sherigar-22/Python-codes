def armstrong_num(n):
    num=[]
    result=0
    n1=n
    while(n1!=0):
        num.insert(0,n1%10)
        n1=n1//10
       

    for i in range(len(num)):
        result+=num[i]**3
    
    if(result==n):
       print(n," is a Armstrong number:")   
    else:
        print(n," is not a Armstrong number:")   

n=int(input("Enter a number :"))
armstrong_num(n)