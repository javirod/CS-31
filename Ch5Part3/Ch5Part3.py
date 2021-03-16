# Week 6, ICA 1
import random

def main():
    total = 0
    print()
    for x in range(1,6):
        # random.seed(25)
        slot = random.randrange(1,10)
        amt = plinkoToss(slot)
        print(f'Disk #{x}: You won ${amt} (slot  = {slot})')
        total += amt
    print(f'You have won ${total:,}')
    if tenGrand(total):
        print("Over $10,000. Great job!")
    else:
        print("Under $10,000. Try again.")
    print()

def plinkoToss(slot):
    if slot == 1 or slot ==  9:
        money = 100
    elif slot == 2 or slot ==  8:
        money = 500
    elif slot == 3 or slot ==  7:
        money = 1000
    elif slot == 5:
        money = 10000
    else:
        money = 0
    return money

def tenGrand(total):
    # if total > 10000:
    #     return True
    # else:
    #     return False
    return total >= 10000
main()