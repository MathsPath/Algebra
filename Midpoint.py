# Midpoint of a line on coordinate plane

# Points of a line
a_point = (-1,-1)
b_point = (4, -3)

def midpoint(point1, point2):
    x = ( point1[0] + point2[0] ) / 2
    y = ( point1[-1] + point2[-1] ) / 2
    return x, y

print(midpoint(a_point,b_point))