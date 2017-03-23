def pi2(i2):
    side = 8
    angle = 135
    distance = 100

    for times in range (1000):
        i2.left(angle)
        i2.circle(times * 10)
        i2.forward(43)
        i2.left(45)
        i2.forward(100)
