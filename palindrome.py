
string=input("Enter a string : ")


def  palindrome(string):
    string1=string[::-1]

    if string1== string:
        print("Its a Palindrome")
        
    else :
        print("Not a Palindrome.")

def symmetrical(string):
    if len(string)%2!=0:
        print("Cannot be symmetrical.")
    else:
        mid=(len(string))//2
        start=0
        end=len(string)
    
        first=string[start:mid]
        last=string[mid:len(string)]
      


        if first==last:
            print("Its symmetrical.") 
        

palindrome(string)
symmetrical(string)