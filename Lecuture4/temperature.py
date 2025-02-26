# Fahrenheit to Celsius function
# C = (F - 32) * (5/9)
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# Celsius to Kelvin Function
# K = C + 273.15
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# # Fahrenheit to Kelvin Function
def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
