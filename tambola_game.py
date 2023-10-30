import time
import random
a=input("ENTER YOUR NAME :")
print("\n WELCOME",a,"\n")
flag=1
while 1:
    while 1:
        n=int(input("ENTER NUMBER OF PLAYERS (NUMBER OF PLAYERS MUST BE GREATER THAN 2 & LESS THAN 10):"))

        list=[]

        if n==2:
            for j in range(0,2):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()


        elif n==3:
            for j in range(0,3):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==4:
            for j in range(0,4):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==5:
            for j in range(0,5):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==6:
            for j in range(0,6):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==7:
            for j in range(0,7):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==8:
            for j in range(0,8):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==9:
            for j in range(0,8):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        elif n==10:
            for j in range(0,10):
                for i in range(0,9):
                    n=random.randint(1,100)
                    list.append(n)
                print("LIST FOR PALYER",j+1,list,"\n")
                list.clear()

        else:
            print("SORRY THE GAME CANNOT BE PLAYED WITH MORE THAN 10 PLAYERS.!\n")
            flag=0
            break
        print("GAME STARTS IN 5 SECONDS")
        time.sleep(5)
        while 1:
            for i in range(0,9):
                print(i+1,"NUMBER IS :",random.randrange(100))
                print("\n DISPLAYING NEXT NUMBER IN 3 SECONDS \n")
                time.sleep(3)
            h=input("IS THERE ANY WINNER (Y/N)?")
            if(h=="y"):
                g=input("ENTER THE NAME OF WINNER.")
                print("CONGRATULATIONS",g,"!!!!!! \n")
                break
            else:
                continue
        d=input("DO YOU WANT TO PLAY AGAIN(Y/N)?")
        if(d=="n"):
            flag==0
            break
        else:
            continue
    if(flag==0):
     continue
    else:
        break

print("\n THANK YOU FOR PLAYING.\n HOPE YOU ENJOYED")