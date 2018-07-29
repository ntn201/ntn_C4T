height = float(input("Your height:(cm) "))/100
weight = float(input("Your weight:(kg) "))

bmi = weight/(height**2)

if bmi < 16:
    print("You are everely underweight")
elif bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You are normal")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are obese")



