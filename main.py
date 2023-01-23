# Python program to convert temperatures to and from celsius, fahrenheit.
temp = int(input("enter temperature: "))
unit = input("enter temperature unit either C or F: ")

if unit.upper() == "C":
    # convert to fahrenheit
    temp = (temp * 9 / 5) + 32
else:
    # convert to celsius
    temp = (temp - 32) * 5 / 9

print(temp)