def leapYear():
    year: int = int(input("Give me a year and I'll tell you if it's a leap year "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("The year is actually a leap year!")
    else:
        print("Sorry, it's not a leap year!")


print("This program will tell you which years are leap years...")

print("")

leapYear()

print("")

print("you're welcome friend!!!")
