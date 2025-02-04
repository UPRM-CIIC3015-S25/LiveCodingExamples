import math

# CIIC 3015 Intro to Programming
# Topic: Expressions and Variables
# Lecture 1 Live Coding Examples

# Some common calculations used in engineering and live

# Converting Fahrenheit to Celsius
# Use input() to prompt the user for the temperature in Fahrenheit:
# °C = (°F - 32) × 5/9
# F = int(input("Enter a temperature in Fahrenheit: "))
# C = (F - 32) * (5 / 9)
# print("Temperature in Celsius is", C)

# Converting Celsius to Fahrenheit
# Use input() to prompt the user for the temperature in Celsius:
# C = int(input("Enter a temperature in Celsius: "))
# F = (C * (9/5)) + 32
# print(f"{C} degrees Celsium correspond to {F} degrees Fahrenheit")


# Perimeter of a rectangle
# Create variables to height and width
# width = 50
# height = 60
# perimeter = 2 * width + 2 * height
# print (f"A rectangle of height {height} and width {width} has perimeter "
#        f"{perimeter}")


# Area of a Circle
# Create variable to store radius
# radius = 100
# area = math.pi * radius * radius
# print(f"The area of a circle of radius {radius} is {area}")



# Distance between two points (x1,y1) and (x2,y2)
# Create variables to store coordinates x1, y1, x2, y2
# distance = sqrt((x1-x2)^2 + (y1-y2)^2)
# x1 = 0
# y1 = 0
# x2 = 3
# y2 = 0
# distance = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
# print(f"The distance between points ({x1},{y1}) and ({x2},{y2}) is {distance}")


# Savings after one year earning simple annual interest
# Create variables to store annual_interest and initial_balance
# initial_balance = 1000
# annual_interest = 10
# final_balance = initial_balance * (1 + (annual_interest / 100))
# print(f"After one year at {annual_interest}% annual interest "
#       f"{initial_balance} will turn into {final_balance}")


# Savings after n years earning compounded annual interest
# Create variables to store annual_interest, initial_balance and number of years
# initial_balance = 1000
# annual_interest = 10
# years = 2
# final_balance = initial_balance * (1+(annual_interest/100)) ** years
# final_balance = round(final_balance, 2)
# print(f"After {years} years at {annual_interest}% interest ${initial_balance} "
#       f"will turn into ${final_balance}")

print("End of Testing")

# Quadratic Formula to find zeros of polynomial ax^2 + bx + c
# Create variables to store coefficients a, b, c


# Area of a triangle given the lengths of its 3 sides a, b, and c (Heron's Formula)
# Create variables to store lengths of three sides side1, side2, side3
# YOUR CODE HERE


print('End of Examples')