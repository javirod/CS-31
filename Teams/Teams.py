# ICA1
def main():
    team = int(input("Enter 1 for the Kings, 2 for the Ducks, 3 for the Knights, 4 for the Coyotes, or any other number to quit: "))
    while team >= 1 and team <= 4:
        if team == 1:
            kings()
        elif team == 2:
            ducks()
        elif team == 3:
            knights()
        else:
            yotes()
        team = int(input("Enter 1 for the Kings, 2 for the Ducks, 3 for the Knights, 4 for the Coyotes, or any other number to quit: "))
    print("That's all!")
def kings():
    print("Los Angeles Kings – began NHL play in 1967")
    print("Home arena is Staples Center")
    print()
def ducks():
    print("Anaheim Ducks – began NHL play in 1993")
    print("Home arena is the Honda Center")
    print()
def knights():
    print("Vegas Golden Knights – began NHL play in 2017")
    print("Home arena is the T-Mobile Arena")
    print()
def yotes():
    print("Arizona Coyotes – began NHL play in 1979 as the Winnipeg Jets")
    print("Moved to Arizona in 1996")
    print("Home arena is the Gila River Arena")
    print()
main()