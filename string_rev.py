string=" This is a string ."
st=string.split()[::-1]
l=[]

for i in st:
      l.append(i)
# printing reverse words
print(" ".join(l))