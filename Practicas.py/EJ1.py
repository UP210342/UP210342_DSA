from fractions import Fraction

x = 1
y = Fraction(1, x + Fraction(1, x + Fraction( 1, x + Fraction(1, x))))
z = 1 / (x + 1 / (x + 1 /(x + 1 /x)))

print('y en decimal= ', z)
print('y= ', y)
