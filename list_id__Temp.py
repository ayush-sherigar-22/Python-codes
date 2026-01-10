a = [1, 2, 3]
b =a
a*=4
print(a,b)


dict = {'a':4, 'b': 3, 'c':6, 'd':80}
print(dict.get('e', "Not there in dict"))

list_rec = [1, 2, 3, 4, 5, 'd' ]
print(id(list_rec), id(list_rec[1]))
print(id(list_rec[0]) == id(list_rec[0]))
