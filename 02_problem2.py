''' Write a python program using 
function to convert Celsius to Fahrenheit.'''

# c = 5*((f-32)/9)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from the user
c = float(input("Enter temperature in Celsius: "))

# Calling the function
f = celsius_to_fahrenheit(c)

# Displaying the result
print(f"Temperature in Fahrenheit is: {f}")
