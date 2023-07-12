year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leep Year")
        else:
            print("Not Leep Year")
    else:
        print("Leap Year")
else:
    print("Not Leep Year")
            