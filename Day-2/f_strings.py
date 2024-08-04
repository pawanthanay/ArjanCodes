###  F-Strings Cheat Sheet

#Basic Usage#
name = "Pawan"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Pawan and I am 25 years old.


#Expressions Inside F-Strings#
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
# Output: The sum of 5 and 10 is 15.


#Calling Functions Inside F-Strings#
def greet(name):
    return f"Hello, {name}!"

print(f"Greeting: {greet('Pawan')}")
# Output: Greeting: Hello, Pawan!


#Using Dictionary Keys#
person = {"name": "Aisha", "age": 25}
print(f"{person['name']} is {person['age']} years old.")
# Output: Aisha is 25 years old.


#Debugging (Using `=`)#
#The `=` specifier is a debugging aid that shows the expression and its value.
value = 42
print(f"{value=}")
# Output: value=42


#Formatting Numbers#

#Fixed-Point Number#
value = 1234.56789
print(f"Fixed-point: {value:.2f}")
# Output: Fixed-point: 1234.57


#Comma as Thousands Separator#
large_number = 1000000
print(f"With commas: {large_number:,}")
# Output: With commas: 1,000,000


#Binary, Octal, and Hexadecimal#
number = 255
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")
# Output: 
# Binary: 11111111
# Octal: 377
# Hexadecimal: ff


#Percentage#
percentage = 0.1234
print(f"Percentage: {percentage:.2%}")
# Output: Percentage: 12.34%


#Padding and Alignment#

#Left Align#
print(f"{'left aligned':<20}")
# Output: left aligned        


#Right Align#
print(f"{'right aligned':>20}")
# Output:         right aligned


#Center Align#
print(f"{'centered':^20}")
# Output:     centered     


#Padding with Characters#
print(f"{'padded with dots':.<20}")
# Output: padded with dots....


#Working with Dates#
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
# Output: Current date and time: 2024-08-03 12:34:56


#Escaping Braces#
print(f"{{This is a literal brace}}")
# Output: {This is a literal brace}


#Multi-line F-Strings#
name = "Aisha"
age = 25
message = (
    f"My name is {name}.\n"
    f"I am {age} years old."
)
print(message)
# Output:
# My name is Aisha.
# I am 25 years old.


#Using Variables in Expressions#
x = 5
print(f"x squared is {x**2}")
# Output: x squared is 25


#Custom Formatting (Width and Precision)#
num = 123.4567
print(f"Number with width 10: {num:10.2f}")
# Output: Number with width 10:     123.46


#Nested F-Strings#
name = "Aisha"
age = 25
info = f"My name is {name} and I am {age} years old."
print(f"Info: {info}")
# Output: Info: My name is Aisha and I am 25 years old.


#Conditional Expressions#


is_nice = True
print(f"Aisha is {'nice' if is_nice else 'not nice'}.")
# Output: Aisha is nice.


#Literals Inside F-Strings#


value = 42
print(f"{value=}")  # Useful for debugging
# Output: value=42


#Precision with Floats#


pi = 3.141592653589793
print(f"Pi to 3 decimal places: {pi:.3f}")
# Output: Pi to 3 decimal places: 3.142

