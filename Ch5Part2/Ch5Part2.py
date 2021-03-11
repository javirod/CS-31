# Week 5, ICA 2

#global constants
CONVERT_KM_TO_MILES = 0.6214
CALORIES_FAT = 9
CALORIES_CARBS = 4

def main():
    kms = float(input("Enter kilometers: "))
    getMiles(kms)
    print()
    fatGrams = int(input("Enter fat grams consumed in a day: "))
    carbGrams = int(input("Enter carbohydrates grams consumed today: "))
    getCalories(fatGrams, carbGrams)

def getMiles(k):
    miles = k * CONVERT_KM_TO_MILES
    print(f'{k:.1f} kilometers = {miles:.1f} miles.')

def getCalories(fat, carb):
    fat_calories = fat * CALORIES_FAT
    carb_calories = carb * CALORIES_CARBS
    print("Consuming", fat, "fat grams gives you", fat_calories, "calories from fat.")
    print("Consuming", carb, "carb grams gives you", carb_calories, "calories from carbs.")
    print("Total calories from fat and carbs today is", fat_calories+carb_calories)

# Don't forget to call main
main()