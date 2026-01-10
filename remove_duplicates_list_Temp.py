number_list = [1, 2, 2, 3, 4, 4]
filtered_list_1 = []

for num in  number_list:
   print(num)
   if num not in filtered_list_1:
        filtered_list_1.append(num)

print(filtered_list_1)

# List comprehension

filtered_list = [num for num in number_list if num not in filtered_list]

print(filtered_list)

