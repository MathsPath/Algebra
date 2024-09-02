# """ Slope == tangent """

# Distances
vertical = 0.0
horizontal = 7.0

def slope(vert, horizon):
    if horizon == 0.0:
        return "Undefined"
    return vert / horizon

print(slope(vert=vertical, horizon=horizontal))


# On the coordinate plane
a_point = (-1.0, -1.0)
b_point = (4.0, -3.0)

def slope_plane(point1, point2):
    return ( point2[-1] - point1[-1] ) / ( point2[0] - point1[0] )

print(slope_plane(point1=a_point, point2=b_point))

