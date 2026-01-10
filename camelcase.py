string=input("Enter a string : .")

l=[]

for i in string:
      if i.isupper():
         i=i.lower()
         l.append(i)
      else:
           i=i.upper()
           l.append(i)

print("".join(l))
