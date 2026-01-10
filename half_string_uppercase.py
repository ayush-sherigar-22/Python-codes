#using slice
def upper(str):
    mid=len(str)//2
    str2=str[mid:len(str)]

    str1=str[0:mid]
    return print(str1+(str2.upper()))

#using for loop
def upper_case(str):
    mid=len(str)//2

    for i in (mid,len(str)-1):
        str[i].upper    

    return str    

str=input("Enter a string: ")
upper(str)
upper_case(str)