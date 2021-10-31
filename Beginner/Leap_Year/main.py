
while True:
    year = int(input("Which year do you want to check (Type 0 to exit)? "))

    if (year == 0):
        break
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("It's a leap year")
            else:
                print("It is not a leap year")
        else:
            print("It's a leap year")
    else:
        print("It is not a leap year")