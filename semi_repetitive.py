def longest_semi_repetitive_substring(s):
        left=0
        max_length=0
        seen={}

        for  right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left  = seen[s[right]] +1
                print( right, " entered")
            print(right," r  ")
            seen[s[right]] =right
            max_length = max(max_length, right-left+1)
            print(s[right],seen[s[right]])
            print (max_length)
            print("\n")
           
     
        return max_length
                                     
str="52233"
print("ans is : ",longest_semi_repetitive_substring(str))