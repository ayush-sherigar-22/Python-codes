def factorial(n):
    ans=1
    if(n==0 or n==1):
    
        print("The factorial of ",n," is ",ans)
    elif(n>0):
      for i in range(1,n+1,+1):
         ans=ans*i 
      print("The factorial of ",n," is ",ans)
    else: print("Invalid input.")

num=int(input("Enter a number :"))
factorial(num)