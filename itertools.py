from itertools import count, accumulate, takewhile


#count till infinity
for i in count():
  #print(i)
  if i>=20:
    break


#running total for a given values
numb=list(accumulate(range(8)))
print(numb)
#   0 
#      0+1=1
#      1+2=3


#considers value only if cond satisfied)
print(list(takewhile(lambda x: x<=12, numb)))