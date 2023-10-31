print("What do you want to do :")
n=int(input ("1.Use calculator \n 2.Check Blood donation eligibility  \n 3.Get DNA count \n 4.Exit \n"))


while(1):

    if(n==1):
       from calculator import Cal 
       
    elif(n==2):
       from disease import Disease

    
    elif(n==3):
        from dna_count import dna
    elif(n==4):
        exit()
        print("Thank You !")
        break
    else:
            print("Wrong input.")
