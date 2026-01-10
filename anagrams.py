def anagram(a,b):
    max=256
    map=[]*max
    if  a == b:
        return 0
   
    else:
        l1=list(a)
        l2=list(b)
        print(l1,l2)
    len1=len(l1)-1
    for i in range (0,len1):
        if map[ord(l1[i])]==0:
              map[ord(l1[i])]=1

    print(map)


a="geeks for geeks"
b="beeks for beeks"

anagram(a,b)