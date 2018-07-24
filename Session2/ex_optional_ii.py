n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i*j) < 10:
            space = "  "
        else:
            space = " "
        print(i * j, end=space)
        if j == n:
            print(end="\n")
