x = -20
y = -1


if x > 0 and y > 0:
    print(f"Point P=({x}, {y}) lies in first quadrant")
elif x < 0 and y > 0:
    print(f"Point P=({x}, {y}) lies in second quadrant")
elif x < 0 and y < 0:
    print(f"Point P=({x}, {y}) lies in third quadrant")
elif x > 0 and y < 0:
    print(f"Point P=({x}, {y}) lies in fourth quadrant")
elif x != 0 and y == 0:
    print(f"Point P=({x}, {y}) lies in X axis")
elif x == 0 and y != 0:
    print(f"Point P=({x}, {y}) lies in Y axis")
else:
    print(f"Point P=({x}, {y}) lies in the origin")
