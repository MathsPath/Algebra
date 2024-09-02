# Midpoint of a line on coordinate plane

# Points of a line
a = input("Input A coordinate (separate with ','): ").split(',')
b = input("Input B coordinate (separate with ','): ").split(',')

def midpoint(point1, point2):
    x = ( float(point1[0]) + float(point2[0]) ) / 2
    y = ( float(point1[-1]) + float(point2[-1]) ) / 2
    return x, y

print(midpoint(a,b))
