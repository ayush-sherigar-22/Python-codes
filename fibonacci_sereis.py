def fibonacci(n):
    n1,n2=0,1
    ans=0
    if(n<=0):
        print("Invalis input")

    elif(n==1):
        print("Fibonacci series upto",n," terms is ",n1)
    
    elif(n==2):
        print("Fibonacci series upto",n," terms is ",n2)

    else:
        print("Fibonacci series upto",n," terms is ")
        print(n1)
        print(n2)
        for i in range(1,n+1,+1):
            ans=n1+n2
            print(ans)
            n1=n2
            n2=ans
        


num=int(input("Enter term limit for Fibonacci series :"))
fibonacci(num)