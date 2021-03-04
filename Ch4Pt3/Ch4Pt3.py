# ICA 3, Part 1
players = int(input("Enter number of players: "))
seasons = int(input("Enter number of seasons: "))
for x in range(players):
    total =  0
    name = input("Enter the name of a hockey player: ")
    for  y in range(1, seasons+1):
        goals = int(input(f'Enter goals scored in season #{y}: '))
        total += goals
    print(name, "has scored", total, "goals in the last", seasons, "seasons.")

# # ICA 3, Part 2
# print()
# BASE_SIZE = 8
# for row in range(BASE_SIZE):
#     for y in range(BASE_SIZE-row):  #or range(BASE_SIZE-row, 0, -1)
#         print("*", end = "")
#     print()
# print()
# NUM_STEPS = 6
# for row in range(NUM_STEPS):
#     for y in range((NUM_STEPS-1)-row): #or range((NUM_STEPS-1)-row, 0, -1)
#         print(" ", end = "")
#     print("#")
# print()
# # ICA 3, Part 3
# rows = 7
# for x in range(rows):
#     for y in range(x):
#         print("$", end="")
#     for z  in range((rows-1)-x):
#         print("#", end="")
#     print()
# print()