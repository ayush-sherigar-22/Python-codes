def sum (dice, num):
    list=[]
    while(num!=0):
     #insert adds values specified(after comma) at the specified index(before comma)
     list.insert(0,num%10)
     print(list)
     num=num//10
     

   
    if (dice%2!=0):
        result=0
        for i in range(len(list)):
            
            if i%2==0:
                result+=list[i]
           
        return print(result)
    else: 

        result=0
        for i in range(len(list)):
           
            if i%2!=0:
                print(list[i])
                result+=list[i]
        return print(result)



dice=int(input("Dice"))
num=int(input("Num"))
sum(dice,num)    
