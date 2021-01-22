x = 1
y = 1

while x < 10:
    multiple = int(x * y)
    print(x, "乘於", y, "等於", multiple) #1 * 1
    y = y + 1 # y = 2
    if y > 9:
        x = x + 1
        y = 1
    elif x > 9:
        break






