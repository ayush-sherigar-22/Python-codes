file=open("demo.txt",'w')
file.write("this is me here writing in file.")
file.close()

file=open("demo.txt",'r')
print(file.read())
file.close()

file=open("demo.txt",'w')
file.write("Hello world.")
file.close()

file=open("demo.txt",'r')
print(file.read())
file.close()

file=open("demo.txt",'a')
file.write("this is me here writing in file.")
file.close()

file=open("demo.txt",'r')
print(file.read())
file.close()