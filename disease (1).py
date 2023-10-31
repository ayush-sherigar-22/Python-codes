class Disease :   
        age=int(input("Enter age:"))
        weight=float(input("Enter weight:"))
        gender=input("Enter gender :") 

        if age>=18 and (gender=="male" and weight>=55) or (gender=="female"and  weight>=45)  : 

                print("Disease = Sugar. Cannot Donate Blood.")


        
        elif 13<age<=18 and  (gender=="male" and weight>=55) or (gender=="female"and  weight>=45):

                print("Disease = Sugar. Cannot Donate Blood.")

        elif age<13:
                print("Under Age. Cannot Donate.")

        else: print("No Disease. Can Donate Blood.")

        import imp_application