def sum(n,m):
    count1=0
    count2=0
    for i in range(1,m+1):
        if i%n==0:
            count1+=i
        else:
            count2+=i
    print(count1,"\n",count2)
    return count2-count1


n=4
m=20
print(sum(n,m))
