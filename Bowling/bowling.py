# ICA1, Parts 1 and 2
game1 = int(input("Enter bowling score for game 1: "))
game2 = int(input("Enter bowling score for game 2: "))
game3 = int(input("Enter bowling score for game 3: "))
avg = (game1 + game2 + game3) / 3
print(f'Your average for the 3 games is {avg:.1f}')
if avg >= 100:
    print("Bowling average meets requirement")
    print("Join league now")
else:
    print("Bowling average too low")
    print("Sign up for bowling classes")

# Part 3
word1 = input("Enter a word with no spaces in it: ")
word2 = input("Enter another word with no spaces in it: ")
if word1 > word2:
    print(word1,"is greater than",word2)
else:
    print(word2,"is greater than",word1)