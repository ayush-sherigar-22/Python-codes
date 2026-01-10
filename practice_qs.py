# 1. Num of Vowels
str_temp = 'Interview'
str_temp = str_temp.lower()
str_vow =['a','e', 'i', 'o', 'u']
vow_count=0
for i in range  (len(str_temp)) :
    if str_temp[i] in str_vow:
        vow_count=vow_count+1
print(vow_count)

# 2. Simplified Version
count = sum(1 for ch in str_temp.lower() if ch in "aeiou")
print(count)
# “Convert the string to lowercase, 
# go through each character, 
# add 1 every time the character is a vowel, 
# and finally sum those 1s.”

# | Syntax    | Meaning             |
# | --------- | ------------------- |
# | `[]`      | Build now           |
# | `()`      | Generate later      |
# | generator | One value at a time |

#Lists store values; generators store logic.

gen = (x*x for x in range(5))
print(gen)
lst = list(gen)
print(lst)
t = tuple(gen)
print(t)

#A generator can be iterated only once. So therefore t would be empty as gen was consumed by for


# 3.  Largest num
list = [-5, -2, -10]
m_num=list[0]
# Without max
for i in range(len(list)):
    
    if list[i]>m_num:
        m_num = list[i]

print(m_num)

# Using max 
print(max(list))


#4.  Second largest list

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


# 5. List ID 

a = [1, 2, 3]
b =a
a*=4
print(a,b)


dict = {'a':4, 'b': 3, 'c':6, 'd':80}
print(dict.get('e', "Not there in dict"))

list_rec = [1, 2, 3, 4, 5, 'd' ]
print(id(list_rec), id(list_rec[1]))
print(id(list_rec[0]) == id(list_rec[0]))



# 6. Odd even 
num = int(input("Input a number : "))
if num%2==0:
    print("Even")

else : 
    print("Odd")


# Interview-Optimized
num =7 
print("Even" if num%2==0 else "Odd")


# 7. Remove Duplicates 

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

#8.  Reverse a string

# opt 1 complicate
str = "python"
l = [str[i-1:i] for i in range(1,len(str)+1)]
print("".join(l[::-1]))

# Opt 2c easy
print(str[::-1])



# Opt 3 Using loop (If slicing not allowed)
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#Option 4: Using built-in function
s = "python"
print("".join(reversed(s)))

# sequence[start : end : step]
# s = "abcdef"
# print(s[::2])
# "ace"
# Takes every 2nd character

# Explanation

# Step = -1

# Traverse sequence backwards
# Only ordered data structures support indexing.


# | Structure | Ordered          | Indexed |
# | --------- | ---------------- | ------- |
# | String    | ✅                | ✅       |
# | List      | ✅                | ✅       |
# | Tuple     | ✅                | ✅       |
# | Range     | ✅                | ✅       |
# | Set       | ❌                | ❌       |
# | Dict      | ❌ (conceptually) | ❌       |


# | Feature           | Ordered | Unordered  |
# | ----------------- | ------- | ---------- |
# | Indexing          | ✅ Yes   | ❌ No       |
# | Fixed position    | ✅ Yes   | ❌ No       |
# | Duplicate allowed | Depends | ❌ No (set) |
# | Fast lookup       | Normal  | Very fast  |
# | Example           | List    | Set        |


# 9.String Palindrome
string_inp = 'Madam'
print(string_inp.lower()==string_inp.lower()[::-1])