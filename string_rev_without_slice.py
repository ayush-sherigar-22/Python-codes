string1 = input("Enter a string : ")

str_2 = "" 

for i in range (len(string1), 0, -1):
    
     str_2  = str_2 + string1[i-1]
    
print("Reversed string is  : " , str_2)