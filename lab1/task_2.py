def sort(x, y, z):
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y
    if x > y:
        x, y = y, x
    return x, y, z

x1, y1, z1 = 5, 4, 8
x2, y2, z2 = 9, 10, 3

print(sort(x1, y1, z1))
print(sort(x2, y2, z2))



