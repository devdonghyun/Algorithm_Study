for i in range(1, 20):
    for j in range(1, 18, 2):
        cal1 = i * j
        cal2 = i * (j+1)
        print(i, "*", j, "=", cal1, "/",
              i, "*", j+1, "=", cal2)
    print(i, "*", 19, "=", i*19)
