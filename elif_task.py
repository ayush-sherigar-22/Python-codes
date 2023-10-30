a=int(input("ENTER YOUR ACHIEVEMENT AMOUNT"))
b=int(input("ENTER YOUR SALARY AMOUNT"))
if 50000<a<100000:
    print("YOU WILL GET 10% INCENTIVE")
    a=a*(10/100)
    b=b+a
    print("YOUR FINAL SALARY AMOUNT IS :",b)
elif 100000<a<150000:
    print("YOU WILL GET 15% INCENTIVE")
    a=a*(15/100)
    b=b+a
    print("YOUR FINAL SALARY AMOUNT IS :",b)
elif 150000<a<200000:
    print("YOU WILL GET 20% INCENTIVE")
    a=a*(20/100)
    b=b+a
    print("YOUR FINAL SALARY AMOUNT IS :",b)
elif a>200000:
    print("YOU WILL GET 25% INCENTIVE")
    a=a*(25/100)
    b=b+a
    print("YOUR FINAL SALARY AMOUNT IS :",b)
else:
    print("BETTER LUCK NEXT TIME")