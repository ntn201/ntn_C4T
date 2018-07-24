for i in range(1, 10):
    for j in range(1, 10):
        if (i*j) < 10:
            space = "  "
        else:
            space = " "
        print(i * j, end=space)
        if j == 9:
            print(end="\n")
