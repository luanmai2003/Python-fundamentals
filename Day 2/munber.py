a = 2
b = 4
c = 5
d = 8
e = 17
f = 3

number1 = a + b
# division always returns a floating point number
number2 = (a + b * c) / d
# classic division returns a float
number3 = e / f
# floor division discards the fractional part
number4 = e // f
# 5 squared
number5 = c ** a
#  8 to the power of 4
number6 = d ** b

print(number1)
# 6
print(f"classic division returns a float: {number2}")
# classic division returns a float: 2.75
print("classic division returns a float: %s" % number3)
# classic division returns a float: 5.666666666666667
print("floor division discards the fractional part: ", number4)
# floor division discards the fractional part:  5
print("5 squared: %s" % number5)
# 5 squared: 25
print("8 to the power of 4: %s" % number6)
# 8 to the power of 4: 4096

# #########################################################################

tax = 17 / 3
price = 10

x = price * tax
y = price + x

result =  round(y, 2)

print( result )
# 66.67