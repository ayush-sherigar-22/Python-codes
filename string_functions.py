#formating string
numbers= [4,5,6]
newstring="Numbers : {0}{1}{2}".format(numbers[0], numbers[1], numbers[2])
print(newstring)

newstring="Numbers : {0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
print(newstring)

date="Date is 0{0}-0{2}-200{1}".format(numbers[0], numbers[1], numbers[2])
print(date)


#join
print("\n"," , ".join(["Apple", "Orange","Banana"]))

#replace
# name=input("Enter name :")
# print("HELLO .".replace(".", name))


# start or end of string 
string1="This is a string."
print(string1.startswith("This"))


print(string1.endswith("string."))


#upper & uppercase
print(string1.upper())

print(string1.lower())


