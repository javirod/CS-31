# ICA2, Parts 1 and 2
game1 = int(input("Enter game 1 score: "))
game2 = int(input("Enter game 2 score: "))
game3 = int(input("Enter game 3 score: "))

# age = int(input("How old are you? "))
avg = (game1+game2+game3) / 3

print(f'Your average is {avg:.1f}')
if avg >= 100:
    print("Bowling average meets requirement")
    if avg < 120:
        print("Join beginner league")
    elif avg < 150:
        print("Join intermediate league")
    else:
        print("Join advanced league")
else:
    print("Bowling average does not meet requirement")

# Parts 3 and 4
num = int(input("Enter a number between 1 and 7: "))
bad = num < 1 or num >7
if bad:
    print("Invalid number")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
else:
    print("Sunday")