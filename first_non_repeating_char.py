string_inp = 'swiss'
dict_temp={}
for i in string_inp:

        if i not in dict_temp.keys():
            dict_temp[i]=1
        else : 
            dict_temp[i] = dict_temp[i]+1

print(dict_temp)
for i in dict_temp.keys():
    if dict_temp[i]==1:
     print(i)
     break