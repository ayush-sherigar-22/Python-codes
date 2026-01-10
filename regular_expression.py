import re


pattern = r"eggs"
  

#looks for exact match. it shloud be present in start 
if re.match(pattern,"andeggseggsbacon"):
    print("Match found")

else:
    print("No match found")


#searches in whole string
if re.search(pattern,"baconeggsbacon."):
     print("Match found")

else:
    print("No match found")





print(re.findall(pattern,"baconeggsbacon eggs egg seggs eggs."))


print(re.search(pattern, "baconeggsbacon eggs egg seggs eggs"))
print(re.match(pattern, "baconeggsbacon eggs egg seggs eggs"))