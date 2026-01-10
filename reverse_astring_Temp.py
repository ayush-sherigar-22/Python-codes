# opt 1 complicate
str = "python"
l = [str[i-1:i] for i in range(1,len(str)+1)]
print("".join(l[::-1]))

# Opt 2c easy
print(str[::-1])



# Opt 3 Using loop (If slicing not allowed)
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#Option 4: Using built-in function
s = "python"
print("".join(reversed(s)))

# sequence[start : end : step]
# s = "abcdef"
# print(s[::2])
# "ace"
# Takes every 2nd character

# Explanation

# Step = -1

# Traverse sequence backwards
# Only ordered data structures support indexing.


# | Structure | Ordered          | Indexed |
# | --------- | ---------------- | ------- |
# | String    | ✅                | ✅       |
# | List      | ✅                | ✅       |
# | Tuple     | ✅                | ✅       |
# | Range     | ✅                | ✅       |
# | Set       | ❌                | ❌       |
# | Dict      | ❌ (conceptually) | ❌       |


# | Feature           | Ordered | Unordered  |
# | ----------------- | ------- | ---------- |
# | Indexing          | ✅ Yes   | ❌ No       |
# | Fixed position    | ✅ Yes   | ❌ No       |
# | Duplicate allowed | Depends | ❌ No (set) |
# | Fast lookup       | Normal  | Very fast  |
# | Example           | List    | Set        |
