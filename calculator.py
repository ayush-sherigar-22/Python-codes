def addition(a,b):
    
    return print("\n Answer to addition is :",a+b,"\n ")

def subtraction(a,b):
    
    return print("\n Answer to subtraction is :",a-b,"\n")

def division(a,b):
    
    return print("\n Answer to division is :",a/b,"\n")

def multiplication(a,b):
    
    return print("\n Answer to multiplication is :",a*b,"\n")

def odd_even(a,b):
    if(a%2==0):
      print("\n ",a,"is even \n")
    else: print("\n", a,"is odd \n")

    if(b%2==0):
        print("\n ",b,"is even \n")
    else: print("\n ",b,"is odd \n")

def exit():
    return print("\n Thank You ! \n")

a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
while(1):
  
    n=int(input ("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Check odd even \n 6.Exit \n Enter a choice :"))

    if(n==1):
        addition(a,b)
    elif(n==2):
        subtraction(a,b)
    elif(n==3):
        multiplication(a,b)
    elif(n==4):
        division(a,b)
    elif(n==5):
        odd_even(a,b)
    elif(n==6):
        exit()
        break
    else:
        print("Wrong input.")

