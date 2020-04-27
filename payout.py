import random

green = [0, 00]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


for a in random.sample(green + red + black, 1):
    if a== 0 or 00:
         print("pay 00 or 0")
         break
    else:
        print("The spin resulted in ", a)
        print("Pay", a)
    if a in black:
        print("Pay black")
    elif a in red:
            print("Pay red")
    if a%2 == 0:
        print("Pay Even")
    elif a%2 != 0  :
        print("Pay odd")
    if a < 18 :
        print("Pay 1 to 18")
    elif a > 18:
        print("Pay 19 to 36")
    
   
