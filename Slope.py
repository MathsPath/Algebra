# """ Slope == tangent """

# Distances
vertical = float(input("Vertical distance: "))
horizontal = float(input("Horizontal distance: "))

def slope(vert, horizon):
    if horizon == 0.0:
        return "Undefined"
    return vert / horizon

print(slope(vert=vertical, horizon=horizontal))


# On the coordinate plane
a = input("Input A coordinate (separate with ','): ").split(',')
b = input("Input B coordinate (separate with ','): ").split(',')

def slope_plane(point1, point2):
    return ( float(point2[-1]) - float(point1[-1]) ) / ( float(point2[0]) - float(point1[0]) )

print(slope_plane(point1=a, point2=b))

