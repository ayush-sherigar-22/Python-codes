def meta(n):
    count=0

    for i in range(1,n+1):
        if (i%2==0) and (i%8==0) and (i%4==0):
            count+=1
        else:
            continue

    return count

n=int(input("Enter a number limit :"))

print(f"Meta numbers between 1 to %d is ",(n))
print(meta(n))
