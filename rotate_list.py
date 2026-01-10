# """ Rotate a list by k-steps
# [1, 2, 3, 4, 5] -> by 2 steps -> [4, 5, 1, 2, 3]

# """

input_string = input("Enter integers separated by spaces : ")
list_inp = [int(x) for x in input_string.split()]

steps = int(input("Enter number of steps to rotate : "))
list_rot = []
for i in range (1, steps+1, 1):
    ele = list_inp.pop()
    list_rot.insert(0,ele)


list_rot  = list_rot.__add__(list_inp)

print("Rotated list is : " , list_rot)
