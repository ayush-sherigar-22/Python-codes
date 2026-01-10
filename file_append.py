file=open(r"C:\Users\ayush\OneDrive\Desktop\codes\Python programming\demo2.txt",'w')
file.write("Hello world.")
file.close()

file=open(r"C:\Users\ayush\OneDrive\Desktop\codes\Python programming\demo2.txt",'r')
print(file.read())
file.close()

file=open(r"C:\Users\ayush\OneDrive\Desktop\codes\Python programming\demo2.txt",'a')
file.write("this is me here writing in file.")
file.close()

file=open(r"C:\Users\ayush\OneDrive\Desktop\codes\Python programming\demo2.txt",'r')
print(file.read())
file.close()