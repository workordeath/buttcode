
def getHours():
    user_input = input("Enter the amount of minutes you worked.")
    if user_input % 5 != 0 or user_input <= 0:
        raise Exception("Invalid time.")
    return user_input / 60

def main():
    hours = getHours()

main()