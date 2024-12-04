# Explain abit about quadratic eqns in form of an eqn
print("Given a quadratic equation in the form of ax^2 + bx + c = 0")

# get the user's input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# calculate the discriminant
d = (b**2) - 4 * a * c
d1 = (4 * a * c) - b**2

# find two solutions
if(d > 0):
    x1 = (-b + d**0.5) / 2 * a
    x2 = (-b - d**0.5) / 2 * a
    print("\nThe solutions are: ", x1, " and ", x2)
elif d < 0:
    a = - b / (2 * a)
    b = ( d1 ** 0.5) / (2 * a)
    print("\nThe solutions are: ", a, " + i", b, " and ", a, " - i", b)
elif d == 0:
    print("\nThe solution is: ", -b / (2 * a))
else:
    print("Invalid input")
