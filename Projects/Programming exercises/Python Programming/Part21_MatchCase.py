# Match case statement = An alternative to using many 'elif' statement
#                       execute some code if a value matches a 'case'
#                       Benefits: cleaner and more readable


def day_week(day = input("What day is it? ")):
    if day == "Monday":
        print("It is Monday")
    elif day == "Tuesday":
        print("It is Tuesday")
    elif day == "Wednesday":
        print("It is Wednesday")
    elif day == "Thursday":
        print("It is Thursday")
    elif day == "Friday":
        print("It is Friday")
    elif day == "Saturday":
        print("It is Saturday")
    elif day == "Sunday":
        print("It is Sunday")
    else:
        print("Invalid")

day_week()


def day_of_week(day = input("What day is it? ")):
    match day:
        case "Monday":
            return "It is Monday"
        case "Tuesday":
            return "It is Tuesday"
        case "Wednesday":
            return "It is Wednesday"
        case "Thursday":
            return "It is Thursday"
        case "Friday":
            return "It is Friday"
        case "Saturday":
            return "It is Saturday"
        case "Sunday":
            return "It is Sunday"
        case _:
            return "Invalid"

print(day_of_week())

def day_valid(day = input("What day is it? ")):
    match day:
        case "Monday" | "Sunday":
            return True
        case "Tuesday" | "Saturday":
            return False
        case _:
            return "Invalid"

print(day_valid())
