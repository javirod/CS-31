# ICA 1
more = 'y'
while more == 'y' or more == "Y":
    number = int(input("Enter a number: "))
    if number > 25:
        print(number, "is greater than 25.")
    else:
        print(number, "is 25 or less.")
    more = input("Wanna do this again? (y/n): ")
# Parts 2 and 3
howhigh = int(input("How big a number you want? "))
print("Number\tCubes")
print("-------------")
for x in range(1,howhigh+1):
    print(x, '\t', x ** 3)
print()
start = int(input("Where you wanna start? "))
end = int(input("Where you wanna end? "))
step = int(input("Step value? "))
print("Number\tCubes")
print("-------------")
for x in range(start,end+1,step):
    print(f'{x:<3,d}', '\t', x ** 3)
# Part 4
for x in range(8, -3, -1):
    print(x, end = ' ')
print()
for x in range(30, 1, -7):
    print(x, end = ' ')
print()