list = [-5, -2, -10]
m_num=list[0]
# Without max
for i in range(len(list)):
    
    if list[i]>m_num:
        m_num = list[i]

print(m_num)

# Using max 
print(max(list))