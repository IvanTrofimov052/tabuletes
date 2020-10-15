import math

i = -1
while i <= 2:
    print("{0:.2f}".format(math.sin((i**2 -5) / (i * 3) + 1)))
    i += 0.3
