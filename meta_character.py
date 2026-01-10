import re


#Dot meta character. means there can b any character in between. number of dosts = number of position
pattern=r"gr.y"

if re.match(pattern,"gray",):
    print("Match found.")

else:
    print("No match found.")




# caret ^ means start with
# dollar $ means ends with
pattern=r"^gr.y$"   #start with g end with y

if re.match(pattern,"gray",):
    print("Match found.")

else:
    print("No match found.")





#character class. match only one of specify character from range
# [] specifies range
pattern=r"[A-Z][A-Z][0-9]"

if re.match(pattern, "AF2"):
    print("Match found.")

else:
    print("No match found.")


# star * allows for zero or more repetitions of previous expression
 
pattern=r"eggs(bacon)*" #eggs should be there, elemnt in () can repeat or be missing

if re.match(pattern, "eggsbacon"):
    print("Match found. ")

else:
    print("No match found. ")




 #groups meaning a collection of a word or words that we want ot match. mentioned in ( )

pattern=r"bread(eggs)*bread"
if re.match(pattern, "breadeggsbread"):
    print("Match found.")

else:
    print("No match found")