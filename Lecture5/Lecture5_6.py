# UPRM CIIC 3015 Spring 2025
# Lecture 5: Strings and Lists

# Live Coding Example 6
# Common list processing patterns

# Determine if element with some property exists
# Sample case determine if a list of numbers has an even number
def even_exists(l):
    for number in l:
        if number % 2 == 0:
            return True
    return False


# Find position of first element with some property
# Sample case: Find position of a word with even length in a list of words
def find_even_word(l):
    for pos in range(0,len(l)):
        if len(l[pos]) % 2 == 0:
            return pos
    return -1


# Count occurrences of elements with some property
# Sample case: Count all integers multiples of k in a list
def count_multiples(l, k):
    count = 0
    for number in l:
        if number % k == 0:
            count += 1
    return count

# Calculate accumulation of elements (e.g. sum, product)
# Sample case: Factorial(n) = 1 x 2 x 3 ... x n
def factorial(n):
    accumulator = 1  # Identity element for *
    for i in range(2,n+1):
        accumulator *= i
    return accumulator

# Find position of max or min
# Sample case: Find position of "largest" word in list of words
def find_largest_word(l):
    max_pos = 0
    for pos in range(0,len(l)):
        # next word is l[pos]
        if l[pos] > l[max_pos]:
            max_pos = pos
    return max_pos

l = ['bienve', 'ana', 'Maria']
largest = find_largest_word(l)
print(f"The largest word is {l[largest]} at position {largest}")
l.sort()
print(l)



