num=int(input("Enter a number :"))
temp=num
rev=0 
while temp>0:
    remainder = temp % 10
    rev= (rev * 10) + remainder
    temp = temp // 10

if num ==rev:
  print('Palindrome')
else:
  print("Not Palindrome")
