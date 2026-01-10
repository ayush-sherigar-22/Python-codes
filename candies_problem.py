def candy_count(amnt, list):
    list2=[]
  
    list2.append(amnt//(list[0]))
    list2.append((amnt%(list[0]))//(list[1]))     
    list2.append(((amnt%(list[0]))%(list[1]))//list[2])
    list2.append((((amnt%(list[0]))%(list[1]))%list[2])//(list[3]))
    list2.append(((((amnt%(list[0]))%(list[1]))%list[2])%(list[3]))//list[4])

    return list2
 
list=[2,3,1,4,5]
amount=7
print("Numnber of candies is :", candy_count(amount,list))