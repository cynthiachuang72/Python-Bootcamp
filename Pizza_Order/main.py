print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want (S, M, or L)? ")
add_pepperoni = input("Do you want pepperoni (Y or N)? ")
extra_cheese = input("Do you want extra cheese (Y or N)? ")

additional_price = 0
if (extra_cheese == 'Y' or extra_cheese == 'y'):
    additional_price += 1
if (size == 'S' or size == 's'):
    base_price = 15
    if (add_pepperoni == 'Y' or add_pepperoni == 'y'):
        additional_price += 2
elif (size == 'M' or size == 'm'):
    base_price = 20
    if (add_pepperoni == 'Y' or add_pepperoni == 'y'):
        additional_price += 3
elif (size == 'L' or size == 'l'):
    base_price = 25
    if (add_pepperoni == 'Y' or add_pepperoni == 'y'):
        additional_price += 3

print("Total price = " + str(base_price + additional_price))