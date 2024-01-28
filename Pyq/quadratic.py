import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = b*b - 4*a*c
square_root_value = math.sqrt(abs(discriminant))

if discriminant > 0:
    print("The roots are real and different")
    print((-b + square_root_value) / (2*a))
    print((-b - square_root_value) / (2*a))
elif discriminant == 0:
    print("The roots are real and they are equal!")
    print(-b / (2*a))
    print(-b / (2*a))
else:
    print("The roots are imaginary, i.e., they are complex!")
    real_part = -b / (2*a)
    imaginary_part = square_root_value / (2*a)
    print(f"{real_part} + {imaginary_part}i")
    print(f"{real_part} - {imaginary_part}i")
