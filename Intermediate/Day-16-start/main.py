# import turtle
#
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "squirtle", "charmander"])
table.add_column("Type", ["electric", "water", "fire"])
print(table)
