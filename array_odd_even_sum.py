def arraysum(arr):
    print(len(arr))
    if len(arr)<= 5 :
        return 0
    
    else:
            odd=arr.split()[0::2]
            even=arr.split()[1::2]
            even.sort()
            odd.sort()
            return int(odd[1]) + int(even[1])

array=input("Enter a array :")

print("Answer is :",arraysum(array))

