list_num = [10, 20, 5, 30, 25]
max_num_list = []


for i in range(len(list_num)):

 num_max = max(list_num)
 max_num_list.append(num_max)
 list_num.remove(num_max)

print(max_num_list[1])

# Optimized version
numbers = [10, 20, 5, 30, 25]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
