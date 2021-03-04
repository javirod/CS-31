# ICA2, Parts 1 and 3
total = 0
howmany =  int(input("\nHow many numbers you  want? "))
while howmany <= 0:
    print("Value must be positive, try  again.")
    howmany = int(input("How many numbers you want? "))
for x in range(1, howmany  + 1):
    num =  int(input(f'Enter number #{x}: '))
    total += num
print(f'The average is {total/howmany:.3f}')
print()

# ICA2, Part  2
total = 0
howmany = 0
num = int(input("Enter a number: "))
while num != -1:
    total += num
    howmany += 1
    num = int(input("Enter a number or -1 to quit: "))
print(f'The average is {total/howmany:.3f}')