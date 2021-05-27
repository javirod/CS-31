import Car

def main():
    myCar = Car.Car('2016', 'Subaru', 'Outback')
    print(myCar) # calls the str function
    for x in range(5):
        myCar.accelerate()
        print('Now speed is', myCar.how_fast(), 'MPH.')
    for x in range(5):
        myCar.brake()
        print('Now speed is', myCar.how_fast(), 'MPH.')
main()