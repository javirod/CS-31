# Week 7, ICA 1
import trig
import algebra

def main():
    choice = 0
    while choice != 5:
        display_menu()
        choice = int(input("Enter choice here: "))

        if choice == 1:
            num = float(input("Enter a number: "))
            s, c, t = trig.trig(num)
            print(f'sin({num}) = {s:.2f}, cos({num}) = {c:.2f}, tan({num}) = {t:.2f}')
        elif choice == 2:
            num = float(input("Enter a number: "))
            cl, fl = algebra.ceilfloor(num)
            print(f'ceil({num}) = {cl}, floor({num}) = {fl}')
        elif choice == 3:
            num = float(input("Enter a number: "))
            ln, lg10 = algebra.logs(num)
            print(f'log({num}) = {ln:.2f}, log10({num}) = {lg10:.2f}')
        elif choice == 4:
            num = float(input("Enter a number: "))
            root, expnum =  algebra.sqrtexp(num)
            print(f'sqrt({num}) = {root:.2f}, exp({num}) = {expnum:.2f}')
        elif choice ==  5:
            print('May the force be  with you, Skywalker...')
        else:
            print("Invalid choice. Try again...")
    
def display_menu():
    print('LIST OF CHOICES')
    print('Enter 1 for trig')
    print('Enter 2 for ceilfloor')
    print('Enter 3 for logs')
    print('Enter 4 for sqrtexp')
    print('Enter 5 to QUIT')

main()
