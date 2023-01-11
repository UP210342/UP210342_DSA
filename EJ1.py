from fractions import Fraction

x = 1
y = Fraction(1, x + Fraction(1, x + Fraction( 1, x + Fraction(1, x))))
print('y= ', y)