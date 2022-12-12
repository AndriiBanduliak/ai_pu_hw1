def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("It's mot a number!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("It's a weekend! :)")
    elif 0 < num < 6:
        print("It's a work day")
    else:
        print("Number outside 7 days")


num = InputNumbers("Enter the number of the day: ")
checkNumber(num)