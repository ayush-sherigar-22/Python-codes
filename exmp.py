def func(a,b):
    if(a<b):
        return func(b,a)
    
    elif(b!=0):
        return(a+func(a,b-1))
    else:
        return 0
ans=func(8,9)
print(ans)