import re

string="My name is John. "
print(string)

pattern=r"John"


#               (what to replace, with wat to repalce, in what to replace)
newstring=re.sub(pattern, "Rob", string)

print(newstring)


