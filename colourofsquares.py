oddletter = ("a", "c", "e", "g")
evenletter = ("b", "d", "f", "h")
oddnumber = (1, 3, 5, 7 )
evennumber = (2, 4, 6, 8)

letter = input("Enter your letter: ")
number = int(input("Enter your number： "))
if letter in oddletter and number in oddnumber:
    print("Black")
elif letter in evenletter and number in oddnumber:
    print("White")
elif letter in oddletter and number in evennumber:
    print("White")
elif letter in evenletter and number in evennumber:
    print("Black")
else:
    print("Error!")
