
a=input("ENTER YOUR NAME :")
print("\n WELCOME",a,"TO ONLNEBUY.COM \n")
b=int(input("INFORMATION ABOUT WHICH PHONE YOU WANT TO BUY? \n 1.iPHONE \n 2.REDMI \n 3.SASMSUNG \n 4.VIVO \n"))
c="""1.MODEL: iPHONE 11 
2.PRICE : RS 54,000
3.COLOR: BLACK
4.CAMERA : 64MP+16MP
5.STORAGE: 128GB+4GB"""

c1="""1.MODEL: iPHONE 12 
2.PRICE : RS 70,000
3.COLOR: BLACK/BLUE/GOLD
4.CAMERA : 64MP+20MP
5.STORAGE: 128+4GB"""

c2="""1.MODEL: iPHONE 13 
2.PRICE : RS 1,19,900
3.COLOR: BLACK/BLUE
4.CAMERA : 64MP+30MP
5.STORAGE: 128GB+6GB
"""
 

n="""1.MODEL: REMDI NOTE 9 PRO 
2.PRICE : RS 25,000
3.COLOR: BLUE/RED
4.CAMERA : 32MP+16MP
5.STORAGE:128GB+6GB"""

n1=""" 1.MODEL: REMDI NOTE 9 
2.PRICE : RS 20,000
3.COLOR: BLUE/BLACK
4.CAMERA : 32MP+12MP
5.STORAGE: 32GB+8GB
"""

n2=""" 1.MODEL: REMDI NOTE 10 PRO 
2.PRICE : RS 28,000
3.COLOR: BLUE/BLACK
4.CAMERA : 64MP+16MP
5.STORAGE: 64GB+8GB
"""

m="""1.MODEL: SAMSUNG GALAXY S8 
2.PRICE : RS 35,000
3.COLOR: RED
4.CAMERA : 16MP+8MP
5.STORAGE: 64GB+4GB"""

m1="""1.MODEL: SAMSUNG A50 
2.PRICE : RS 22,000
3.COLOR: RED/BLACK
4.CAMERA : 32MP+12MP
5.STORAGE: 64GB+8GB"""

m2="""1.MODEL: SAMSUNG M40
2.PRICE : RS 20,000
3.COLOR: BLUE
4.CAMERA : 32MP+8MP
5.STORAGE: 32GB+16GB"""

k="""1.MODEL: VIVO X 60
2.PRICE : RS 28,000
3.COLOR: BLUE
4.CAMERA : 16MP+8MP
5.STORAGE: 64GB+8GB"""

k1="""1.MODEL: VIVO X50
2.PRICE : RS 47,000
3.COLOR: BLUE
4.CAMERA : 36MP+16MP
5.STORAGE: 32GB+16GB"""


k2="""1.MODEL: VIVO V19
2.PRICE : RS 28,000
3.COLOR: BLUE
4.CAMERA : 16MP+8MP
5.STORAGE: 32GB+16GB"""

if(b==1):
    print("MODELS AVAILABLE:\n")
    print(c,"\n")
    print(c1,"\n")
    print(c2,"\n")
    s=input("DO YOU WANT TO PURCHASE ANY OF THESE?(Y/N) ")
    if(s=='y'):
        print("OFFERS AVAILABLE RIGHT NOW!!!!")
elif (b==2):
    print("MODELS AVAILABLE:\n")
    print(n,"\n")
    print(n1,"\n")
    print(n2,"\n")
    s=input("DO YOU WANT TO PURCHASE ANY OF THESE?(Y/N) ")
    if(s=='y'):
         print("OFFERS AVAILABLE RIGHT NOW!!!!")
        
elif(b==3):
    print("MODELS AVAILABLE:\n")
    print(m,"\n")
    print(m1,"\n")
    print(m2,"\n")
    s=input("DO YOU WANT TO PURCHASE ANY OF THESE?(Y/N) ")
    if(s=='y'):
         print("OFFERS AVAILABLE RIGHT NOW!!!!")
elif(b==4):
    print("MODELS AVAILABLE:\n")
    print(k,"\n")
    print(k1,"\n")
    print(k2,"\n")
    s=input("DO YOU WANT TO PURCHASE ANY OF THESE?(Y/N) ")
    if(s=='y'):
        print("OFFERS AVAILABLE RIGHT NOW!!!!")
else:
    print("INVALID INPUT")


j=input("DO YOU WANT TO PURCHASE NOW?(Y/N) ")
if(j=='y'):
    a=int(input("\n ENTER THE AMOUNT OF MODEL YOU WANT TO BUY:"))
    if 15000<a<25000:
        print("YOU GOT 30% DISCOUNT")
        a=a-(a*(30/100))
        print("YOUR FINAL AMOUNT IS :",a)
    elif 25000<a<50000:
        print("YOU GOT 40% DISCOUNT")
        a=a-(a*(40/100))
        print("YOUR FINAL AMOUNT IS :",a)
    elif a>50000:
        print("YOU GOT 50% DISCOUNT")
        a=a-(a*(50/100))
        print("YOUR FINAL AMOUNT IS :",a)
    else:
        print("SORRY NO OFFERS AVAILABLE FOR THIS AMOUNT OF SHOPPING.")

a=int(input("SELECTYOU PAYMENT METHOD:\n 1.CASH ON DELIVERY \n 2.CREDIT CARD \n 3.GPAY \n 4.PAYTM \n\n"))        
list1=[2,3,4]
if(a in list1):
    print("CONGRATULATIONS YOU RECIEVED Rs500 VOUCHER FOR YOUR NEXT SHOPPING:")
print("\nPAYMENT RECIEVED \n YOUR ORDER WILL BE DELIVERED SOON \nTHANK YOU.KEEP SHOPPING WITH US !!")

