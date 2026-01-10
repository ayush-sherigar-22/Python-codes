#using len func
def len_func(str):
    len(str)
	
#using while
def while_len(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

#using for
def for_len(str):
	counter=0
	for i in str:
		counter+=1
	return counter

#using random string
def random_str(str):

	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(while_len(str))
print(for_len(str))
print(len_func(str))
print(random_str(str))


