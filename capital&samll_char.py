ch=ord(input("Enter a character : "))   #ord='order' is use to convert character value to ascii


if ch>=65 and ch<=91:
    print(ch," is small character. ")

elif ch>=97 and ch<=122:
    print(ch," is capital character. ")

elif ch>=46 and ch<=57:
    print(ch," is digit. ")

else:
    print(ch,"is a special character.")
