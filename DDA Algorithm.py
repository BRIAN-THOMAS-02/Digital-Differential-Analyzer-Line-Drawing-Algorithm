print("DDA Method")

x0 = int(input("Enter X0 : "))
y0 = int(input("Enter Y0 : "))
xn = int(input("Enter Xn : "))
yn = int(input("Enter Yn : "))

dx = xn - x0
dy = yn - y0

print(" ")
print("Dx : ", dx, "   Dy : ", dy)

if (dx > dy):
    length = dx
else:
    length = dy

print("Length : ", length)

delta_x = (xn - x0) / length
delta_y = (yn - y0) / length

print("Delta X : ", delta_x, "    Delta Y : ", delta_y)
print(" ")

if (delta_x < 0):
    sign = -1
    x = x0 + 0.5 * sign
    y = y0 + 0.5 * sign

elif(delta_x == 0):
    sign = 0
    x = x0 + 0.5 * sign
    y = y0 + 0.5 * sign

elif(delta_x > 0):
    sign = 1
    x = x0 + 0.5 * sign
    y = y0 + 0.5 * sign

print("|  ", "i", "  |",  "  X  ", " ", "|", "  Y  ", "|", "     Plot", "   |")
i = 0
while i <= length:
    i = i + 1
    print("|  ", i, "  |  ", int(x), "  ", " |  ", int(y), "  |  ", "(", int(x), ",", int(y), ")", " |")
    x = x + delta_x
    y = y + delta_y


