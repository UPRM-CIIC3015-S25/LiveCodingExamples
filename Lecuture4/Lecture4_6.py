import time

# UPRM CIIC 3015 Spring 2025
# Lecture 4: Loops and Iteration
# Live Coding Examples

# Function to print all even numbers from n to m using a for loop with range
def print_evens(n, m):
    if n%2 != 0:
        n+=1
    for i in range(n, m+1, 2):
        print(i)

# print_evens(3, 11)


# Function to print all multiples of k from 0 to N
def print_multiples_of_k(n, k):
    for i in range(n+1):
        if i % k == 0:
            print(i)

# print_multiples_of_k(100, 7)




# Boolean function to determine if a number is prime
def is_prime(n):
    for factor in range(2,n):
        if n%factor == 0:
            print(f"{factor} divides {n}")
            return False
    return True

# print(is_prime(11)) # True
# print(is_prime(1234567321097)) # No clue
# print(is_prime(21)) # False



# Function to print a triangle pattern of '*' (Nested Loops)

def print_rectangle(n,m):
    print('\n')
    for i in range(0, n):
        for j in range (0,m):
            print('*', end='')
        print('')


def print_triangle(n,m):
    print('\n')
    for i in range(0, n):
        for j in range (0,i+1):
            print('*', end='')
        print('')

print_triangle(10,20)

print("End of Problems")

