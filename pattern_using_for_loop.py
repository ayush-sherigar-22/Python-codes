"""
*
**
***
****
"""
def pattern1(n):
    for i in range(1,n+1,+1):
        for j in range(0,i,+1):
         print(" * " , end=" ")
        print("\n")   
 




"""
 * * * *
 * * *
 * *
 *
 """
def pattern2(n):
   for i in range(0,n,+1):
      for j in range(n,i,-1):
          print(" * " , end=" ")
      print("\n")   





"""
     *
    * *
   * * *
  * * * *
  """
def pattern3(n):
    for i in range(1,n+1,+1):
      for j in range(n,i,-1):
         print(" ", end=" ")
      for k in range(0,i,+1):
        print(" * ",end=" ")
      for l in range (n,i,-1):
         print(" ", end=" ")
      print("\n")     




"""
1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 """

def pattern4(n):
   
    for i in range(1,n+1,+1):
        for j in range(0,i,+1):
         ans=1
         ans+=j
         print(ans , end=" ")
        print("\n")       






"""
1 

2 3 

4 5 6 

7 8 9 10 
"""

def pattern5(n):
     ans=0
     for i in range(1,n+1,+1):
       for j in range(0,i,+1):
        
         ans+=1
         print(ans , end=" ")
       print("\n")     





"""
A 

B B 

C C C 

D D D D 
"""

def pattern6(n):
    ans=65
    for i in range(1,n+1,+1):
        
        ch=chr(ans)
        for j in range(0,i,+1):
         print(ch , end=" ")
        print("\n")  
        ans+=1 
        


"""
A 

A B 

A B C 

A B C D 
"""

def pattern7(n):

    for i in range(0,n,+1):
       ans=65
       ch=chr(ans)
       for j in range(0,i,+1):
         print(ch , end=" ")
         ans+=1
         ch=chr(ans)
       print("\n")  
   


"""
A 

B C 

D E F 

G H I J 

"""

def pattern8(n):
    ans=65
    ch=chr(ans)
    for i in range(0,n,+1):
      
       for j in range(0,i,+1):
         print(ch , end=" ")
         ans+=1
         ch=chr(ans)
       print("\n")  





"""     *
      * *
    * * *
  * * * *"""


def pattern9(n):
    for i in range (0,n,+1):
       for j in (i,n-i,+1):
          print(" ",end=" ")
        
       for k in range(0,i,+1):
          print(" * ",end="")
       print("")
          
   

pattern9(5)