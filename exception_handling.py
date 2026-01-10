# try:
#     a=int(input("Enter a number "))
#     b=int(input("Enter number"))
#     print("Ans is ",a/b)
# except ZeroDivisionError:
#     print("Enter a another number")


try:
    a=int(input("Enter a number :"))

except ValueError:
    print("Enter a appropriate value")
finally: 
    print("END")

# try:
#     a=int(input("Enter a number "))


# except TypeError:
#     print("Enter a another number")

##Finally block will execute no mateer if error is found or not