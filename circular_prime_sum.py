import math

def cir_prime_sum(rangeMax,rangeMin):
   
    answer=[]
 #iterate through the range
    for i in range(rangeMin,rangeMax):
        temp=[]
#check if number is prime      
        if(is_prime(i)):
            #if the number is prime then reverse it and check if thats prime
            if(is_prime(reverse(i))):
                #if its circular then append to final list
                answer.append(i)
                
        else:
            continue
        

    ans=0
    print(answer)
    #addition of circular prime numbers
    for i in range(len(answer)):
        ans=answer[i]+ans

    return print(ans)

def reverse(n):
    p=((n%10)*10)+(n//10)
    return p


def is_prime(n):
    flag=True
    #to check if number is prime of not iterate till its square root. 
    # #using ceil to round off non perfect squares
    for i in range(2,math.ceil(math.sqrt(n))):
        if(n%i)==0:
            flag=False
            break
        else:
            continue
    if(flag):
        return True
    else: 
        return False

rangeMin=60
rangeMax=80

cir_prime_sum(rangeMax,rangeMin)