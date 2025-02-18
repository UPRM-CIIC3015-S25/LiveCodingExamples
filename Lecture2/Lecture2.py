# UPRM CIIC 3015 Spring 2025
# Lecture 2: Decisions and Boolean Logic
# Live Coding Examples

# Use an if statement to calculate your final CIIC 3015
# letter grade given your final numeric score
numeric_score = 75.23
if numeric_score >= 90:
    letter_grade = 'A'
    print(f"A score of {numeric_score} yields a {letter_grade}")
elif numeric_score >= 80:
    letter_grade = 'B'
    print(f"A score of {numeric_score} yields a {letter_grade}")
elif numeric_score >= 70:
    letter_grade = 'C'
    print(f"A score of {numeric_score} yields a {letter_grade}")
elif numeric_score >= 65:
    letter_grade = 'D'
else:
    letter_grade = 'F'
    print(f"A score of {numeric_score} yields a {letter_grade}")
print(f"A score of {numeric_score} yields a {letter_grade}")

# Use an if statement to calculate the number of real
# roots of a polynomial with float coefficients a, b, c
a = 1.0
b = 5.0
c = 6.0
discriminant = b * b - 4 * a * c
if discriminant == 0:
    real_roots = 1
elif discriminant < 0:
    real_roots = 0
else:
    real_roots = 2  
print(f"Polynomial {a}x^2 + {b}x + {c} has {real_roots} real roots")

print('End of tests')

# Use if statements to determine the color resulting from
# combining two of primary colors red, blue and yellow.
color1 = 'blue'
color2 = 'red'
color3 = 'yellow'
# YOUR CODE HERE
# print(f"Combine {color1} with {color2} to get {combined_color}")

# Use if statement to implement a "Change for a Dollar"
# game.  The user enters an amount of quarters, dimes,
# nickles and pennies and wins if these coins add up to
# one dollar
# quarters = int(input("Number of quarters: "))
# dimes = int(input("Number of dimes: "))
# nickles = int(input("Number of nickles: "))
# pennies = int(input("Number of pennies: "))
# YOUR CODE HERE