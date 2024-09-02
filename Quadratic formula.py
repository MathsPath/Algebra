import math

a = float(input("Input A value: "))
b = float(input("Input B value: "))
c = float(input("Input C value: "))


def quadratic(a_value, b_value, c_value):
    if b_value**2 - 4 * a_value * c_value < 0:
        return "Quadratic has 0 roots, no x-intercepts"

    if c_value < 0:
        print(f"\n{a_value}x\u00b2 + {b_value}x - {c_value * -1} = 0")
    else:
        print(f"\n{a_value}x\u00b2 + {b_value}x + {c_value} = 0")

    positive_x = ( -b_value + math.sqrt(b_value**2 - 4 * a_value * c_value)) / 2 * a_value
    negative_x = ( -b_value - math.sqrt(b_value**2 - 4 * a_value * c_value)) / 2 * a_value

    return positive_x, negative_x

print(quadratic(a_value=a, b_value=b, c_value=c))