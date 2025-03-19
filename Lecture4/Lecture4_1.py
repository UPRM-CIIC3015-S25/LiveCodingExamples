import time

# UPRM CIIC 3015 Spring 2025
# Lecture 4: Loops and Iteration
# Live Coding Examples

# Function read a password until it is correct
def get_password():
    password = ''
    while password != 'helloworld':
        password = input('Password?')
        if password == 'helloworld':
            print('Access granted!')
        else:
            print('Wrong password.')
    print("The End")


# Function to print numbers from 1 to n
def print_1_to_n(n):
    next_number = 1
    while next_number <= n:
        print(f"Next number is {next_number}")
        next_number += 1
    print("End of while")

# print(print_1_to_n(4))

#Function to decrement a timer every second until it reaches 0
def countdown(secs):
    while secs > 0:
        print(f"{secs} seconds to blastoff")
        time.sleep(1)
        secs -= 1
    print("Blastoff!!!")

# countdown(10)

# while True:
#     print("Infinite")

def print_rectangle(n,m):
  print('\n')
  for i in range(0, n):
    for j in range (0,m):
       print('*', end='')
    print('')

print_rectangle(10,20)


print("End")







