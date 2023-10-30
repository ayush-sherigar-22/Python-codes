amount=int(input("Entyer amount  for withdraw :"))

print("100 notes  : ",amount//100)
print("50 notes  : ",(amount%100)//50)
print("20 notes  : ",((amount%100)%50)//20)
print("10 notes  : ",(((amount%100)%50)%20)//10)