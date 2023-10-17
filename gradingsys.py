math = int(input("Enter Math grade:"))
physics = int(input("Enter physics grade:"))
geo = int(input("Enter Geography grade:"))
chem = int(input("Enter Chemistry grade:"))


if 0 <= math <= 30:
    print("You got a D in Math")
elif 31 <= math <= 50:
    print("You got a C in Math")
elif 51 <= math <= 70:
    print("You got a B in Math")
elif 71 <= math <= 100:
    print("You got an A in Math")
else:
    print("Math grade is unrecognized (0-100)")

if 0 <= geo <= 30:
    print("You got a D in Geography")
elif 31 <= geo <= 50:
    print("You got a C in Geography")
elif 51 <= geo <= 70:
    print("You got a B in Geography")
elif 71 <= geo <= 100:
    print("You got an A in Geography")
else:
    print("Geography grade is unrecognized (0-100)")

if 0 <= chem <= 30:
    print("You got a D in Chemistry")
elif 31 <= chem <= 50:
    print("You got a C in Chemistry")
elif 51 <= chem <= 70:
    print("You got a B in Chemistry")
elif 71 <= chem <= 100:
    print("You got an A in Chemistry")
else:
    print("Chemistry grade is unrecognized (0-100)")

average = (math + physics + geo + chem) / 4

print(f"Your average grade is {average}")