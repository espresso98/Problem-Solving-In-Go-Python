from bmi import BMI

x = BMI()
y = BMI()

x.height = 2
x.weight = 75
y.height = 2
y.weight = 76

print(x._BMI__pHeight)
print(x._BMI__pWeight)
print(x.BMI_value())

if x == y:
    print("They are equal")
else: print("They are not equal")

