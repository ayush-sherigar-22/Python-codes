def check (n,list):
    
    result=0

   
    if (n%2!=0):
        
        for i in range(0,n-1):
          if(i%2!=0):
            if ((list[i])%2!=0):
                result+=1
                
        return print(result)
    
    else: 
        print(list)
        
        for i in range(0,n-1):
           if(i%2==0):
            if ((list[i])%2==0):
                    result+=1
        
        return print(result)




n=int(input("Enter  size of array"))
list=[]
print("Enter array values:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
check(n,list)    
