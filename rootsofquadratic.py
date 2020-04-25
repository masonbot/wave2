a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c = int(input("Enter value for c:"))

d = (b**2) - 4*a*c

if d > 0:
    print("2 real roots")
elif d == 0:
    print("1 real root")
elif d < 0:
    print("No real roots")
else:
    print("Insert real whole number")