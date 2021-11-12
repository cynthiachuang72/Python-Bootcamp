import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_choices = [rock, paper, scissors]
cpu_random_choice = random.choice(game_choices)

your_choice = input("Rock, paper, or scissors? ")
if (your_choice.casefold() == 'rock'):
    print("Your choice is\n", rock)
    print("\nCPU's choice is\n", cpu_random_choice)
    if (cpu_random_choice == rock):
        print("You're tied")
    elif (cpu_random_choice == paper):
        print("You lose")
    else:
        print("You win")
elif (your_choice.casefold() == 'paper'):
    print("Your choice is\n", paper)
    print("\nCPU's choice is\n", cpu_random_choice)
    if (cpu_random_choice == paper):
        print("You're tied")
    elif (cpu_random_choice == scissors):
        print("You lose")
    else:
        print("You win")
else:
    print("Your choice is\n", scissors)
    print("\nCPU's choice is\n", cpu_random_choice)
    if (cpu_random_choice == scissors):
        print("You're tied")
    elif (cpu_random_choice == rock):
        print("You lose")
    else:
        print("You win")