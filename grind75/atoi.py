# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

"""
Approach:
- We have a string; we can get the ascii code from ord()
- We also have the length of the string and want to get the sign as either positive or negative
- We could have an integer and we keep adding to it based on the location of the char in the string; we do need to know the length and where the '.' is to know how many positions until .

Steps
- Get length of string after stripping whitespace
- Get location of '.' if there's any
"""

def myAtoi(s: str) -> float:
    stripped = s.strip()

    sign = 0
    if '-' in stripped:
        sign = -1
        stripped = stripped.replace('-','')
    elif '+' in stripped:
        sign = 1
        stripped = stripped.replace('+','')

    dot_index = stripped.find('.') # if -1 no .

    num_magnitude = 0
    dec_magnitude = 0

    if dot_index != -1:
        numbers = stripped[:dot_index]
        num_magnitude = len(numbers)
        decimals = stripped[dot_index+1:] # skip '.'
        dec_magnitude = len(decimals)
    else: # no decimals
        numbers = stripped
        num_magnitude = len(numbers)

    number = 0.0
    for i in range(num_magnitude):
        num = ord(numbers[i]) - 48 # '0' starts at 48 up to '9' at 57
        power10 = (10**(num_magnitude-i-1))
        number += num * power10
    for i in range(dec_magnitude):
        num = ord(decimals[i]) - 48 # '0' starts at 48 up to '9' at 57
        power10 = (10**-(i+1))
        number += num * power10

    if sign == 0:
        print(f"number: {number}")
        return number

    print(f"sign: {sign}, number: {number}")
    return sign * number

# myAtoi('123')
# myAtoi('12.123')
myAtoi('-123')
