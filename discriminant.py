import math
from decimal import Decimal

print('A program for solving quadratic equations through a discriminant, do not forget about the minuses in the coefficients')
a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))

d = math.pow(b, 2) - 4 * a * c

if d < 0:
    print('No roots')
elif d > 0:
    x1_ = -1 * b - math.sqrt(d)
    x1 = x1_ / 2 / a
    x2_ = -1 * b + math.sqrt(d)
    x2 = x2_ / 2 / a
    print('x1 =', Decimal(str(x1)).as_integer_ratio())
    print('x2 =', Decimal(str(x2)).as_integer_ratio())
elif d == 0:
    x_ = -1 * b
    x = x_ / 2 / a
    print('x =', Decimal(str(x)).as_integer_ratio())
else:
    print('What the fuck is this...')