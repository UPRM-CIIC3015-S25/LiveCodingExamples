# UPRM CIIC 3015 Spring 2025
# Lecture 7: recursion

# Live Coding Example 7_2

# Recursion

# Remove all occurrences of a key within a list
def remove_all(l, key):
    if len(l) == 0:
        return []
    elif l[0] == key:
        return remove_all(l[1:],key)
    else: # Must be true that l[0] != key
        return [l[0]] + remove_all(l[1:],key)


print(f"Removing zeros from {[1,2,3,0,5,6,0]} yields {remove_all([1,2,3,0,5,6,0],0)}")

# Remove first k Occurrences of a key within a list
def remove_k(l, key, k):
    if len(l) == 0 or k == 0:
        return l
    elif l[0] == key:
        return remove_k(l[1:],key,k-1)
    else:
        return [l[0]] + remove_k(l[1:], key, k)


print(f"Removing 2 zeros from {[1,0,3,0,5,6,0]} yields {remove_k([1,0,3,0,5,6,0],0, 2)}")
print(f"Removing 1000 zeros from {[1,0,3,0,5,6,0]} yields {remove_k([1,0,3,0,5,6,0],0, 1000)}")

# Replace all occurrences of a key within a list
def replace_all(l, key, sub):
    if len(l) == 0:
        return l
    elif l[0] == key:
        return [sub] + replace_all(l[1:],key,sub)
    else:
        return [l[0]] + replace_all(l[1:],key,sub)


print(f"Replacing all zeros for -1 in  {[1,0,3,0,5,6,0]} yields {replace_all([1,0,3,0,5,6,0],0, -1)}")


# Replace first k Occurrences of a key within a list
# Replace all occurrences of a key within a list
def replace_k(l, key, sub, k):
    if len(l) == 0 or k == 0:
        return l
    elif l[0] == key:
        return [sub] + replace_k(l[1:],key,sub,k-1)
    else:
        return [l[0]] + replace_k(l[1:],key,sub,k)


print(f"Replacing 2 zeros for -1 in  {[1,0,3,0,5,6,0]} yields {replace_k([1,0,3,0,5,6,0],0, -1, 2)}")
