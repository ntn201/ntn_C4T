factorial = 1
n = int(input("n = "))

for i in range(n):
    factorial *= (i + 1)
print("Factorial of", n, "is", factorial)
