dict={"Name":"Zara","Age":"12","Class":"5"}
print("Dict is:",dict)
print("Value is:",dict["Name"])
print("Value is:",dict["Age"])


dict={"Name":"Zara","Age":"12","Class":"5"}
dict["Age"]="8" #updates value
dict["School"]="DPS" #ADDS NEW VALUE
print("Dict is:",dict)
print("Value is:",dict["School"])
print("Value is:",dict["Age"])

dict={"Name":"Zara","Age":"12","Class":"5"}
del dict["Name"]
print("Dict is:",dict)
dict.clear() #removes all entries
del dict #del entire dict
print("Dict is:",dict)
print("Value is:",dict["School"])
print("Value is:",dict["Age"])



dict={"Name":"Zara","Age":"12","Class":"5","Name":"Asmi"}
print("Value is:",dict["Name"])



dict={"Name":"Zara","Age":"12","Class":"5","Name":"Asmi"}
print("Len is: %d"%len(dict))


dict={"Name":"Zara","Age":"12","Class":"5","Name":"Asmi"}
print("String  is:%s" %str(dict))


dict={"Name":"Zara","Age":"12","Class":"5","Name":"Asmi"}
print("Variable is:%s" %type(dict))


dict={"Name":"Zara","Age":"12","Class":"5","Name":"Asmi"}
print("Len is: %d"%len(dict))
dict.clear()
print("Len is: %d"%len(dict))


dict={"Name":"Zara","Age":"12","Class":"5"}
dict2=dict.copy()
print("Dict 2 is:",dict)
dict3=dict.fromkeys(dict,10)
print("Dict 3 is:%s"%str(dict3))

dict={"Name":"Zara","Age":"12","Class":"5"}
print("Value is: %s"%dict.get("Age"))
print("Value is: %s"%dict.get("Sex","Female"))


dict={"Name":"Zara","Age":"12","Class":"5"}
print("Value is: %s"%dict.items())


dict={"Name":"Zara","Age":"12","Class":"5"}
print("Value is: %s"%dict.keys())


dict={"Name":"Zara","Age":"12","Class":"5"}
print("Value is: %s"%dict.setdefault("Age",None))
print("Value is: %s"%dict.setdefault("Sex",None))


dict={"Name":"Zara","Age":"12","Class":"5"}
dict2={"Sex":"Female"}
dict.update(dict2)
print("Updaed dict  is:",dict)

dict={"Name":"Zara","Age":"12","Class":"5"}
print("Value is: ",list(dict.values()))

