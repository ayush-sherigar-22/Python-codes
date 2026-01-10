numbers={1,2,3,4,5,6,7}
print(numbers)
print(5 in numbers)

numbers.add(9)
print(numbers)

numbers.remove(4)
print(numbers)

numbers2={11,12,13,14,15,16,17, 9, 4}

#union
print(numbers | numbers2)


#intersection
print(numbers&numbers2)