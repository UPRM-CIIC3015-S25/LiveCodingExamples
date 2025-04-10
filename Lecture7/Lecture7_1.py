# UPRM CIIC 3015 Spring 2025
# Lecture 6: Dictionaries and Sets

# Live Coding Example 7
# Recursion

# Generate list of integers from "first" to "last" recursively
def my_range(first, last):
    pass

# Version 2: More efficient
def my_range2(first, last):
    pass


print(f"Numbers from {0} to {10} are: {my_range2(0,10)}")


# Calculate the sum of the numbers in a list recursively
def sum_list(l):
    pass

print(f"Sum of numbers in [1,2,3,4,5] is: {sum_list([1,2,3,4,5])}")


# Calculate a to the bth power recursively
def my_pow(a,b):
    pass

print(f"{5} to the {3} power is: {my_pow(5,3)}")



# Determine if a string is a palindrome recursively
def is_palindrome(w):
    pass

print(f"Word \'{'radar'}\' is a palindrome? {is_palindrome('radar')}")
print(f"Word \'{'bienve'}\' is a palindrome? {is_palindrome('bienve')}")
print(f"Word \'{'b'}\' is a palindrome? {is_palindrome('b')}")
print(f"Word \'{''}\' is a palindrome? {is_palindrome('')}")

# Find the maximum among a list of numbers
# Assume the list is not empty
def max_recursive(l):
    pass


print(f"Maximum number in {[1,2,3,4,5]} is {max_recursive([1,2,3,4,5])}")
print(f"Maximum number in {[5,4,3,2,1]} is {max_recursive([5,4,3,2,1])}")
print(f"Maximum number in {[5]} is {max_recursive([5])}")


# Reverse a string recursively
def reverse_recursive(w):
    pass

print(f"Reverse of {"bienvenido"} is: {reverse_recursive("bienvenido")}")
print(f"Reverse of {""} is: {reverse_recursive("")}")
print(f"Reverse of {"b"} is: {reverse_recursive("b")}")


#Return a list with all permutations of a string
def permutations(w):
    if len(w) <= 1:
        return [w]
    else:
        result = []
        for i in range(len(w)):
            letter = w[i]
            shorter_w = w[0:i] + w[i+1:]
            sub_perms = permutations(shorter_w)
            for sub_word in sub_perms:
                long_word = letter + sub_word
                result.append(long_word)
        return result

print(f"Permutations of {'eat'} are: {permutations('eat')}")

print(f"Permutations of {'eats'} are: {permutations('eats')}")
print(f"Permutations of {'bienve'} are: {permutations('bienve')}")


def base_convert(n,b):
    digits = '0123456789ABCDF'
    if n < b:
        return digits[n]
    else:
        return base_convert(n//b, b) + digits[n%b]

print(f"Number {57} in base {16} is {base_convert(57,16)}")
print(f"Number {57} in base {3} is {base_convert(57,3)}")
print(f"Number {57} in base {2} is {base_convert(57,2)}")

