Month = input("Input your month:")

if Month == "February":
    print("28 or 29 days")
elif Month in ("April", "June", "September", "November"):
    print("30 days")
elif Month in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 days")
else: 
    print("Error!")
