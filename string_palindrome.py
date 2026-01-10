def is_palindrome(str1):
    temp=str1.split()[::-1]
    print(temp)
    list=[]
    for i in temp:
        list.append(i)
    print(join(list))
    


str='abc'
is_palindrome(str)