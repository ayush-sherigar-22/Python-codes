a=int(input("ENTER YOUR SHOPPING TOTAL"))
if 1000<a<5000:
    print("YOU GOT 30% DISCOUNT")
    a=a-(a*(30/100))
    print("YOUR FINAL AMOUNT IS :",a)
elif 5000<a<10000:
    print("YOU GOT 40% DISCOUNT")
    a=a-(a*(40/100))
    print("YOUR FINAL AMOUNT IS :",a)
elif a>10000:
    print("YOU GOT 50% DISCOUNT")
    a=a-(a*(50/100))
    print("YOUR FINAL AMOUNT IS :",a)
else:
    print("BETTER LUCK NEXT TIME")
print("THANK YOU FOR SHOPPING !!!!")  