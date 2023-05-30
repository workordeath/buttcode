
def getHours():
    print("Enter the amount of minutes you worked.")
    
    try:
        user_input = int(input(">> "))

        if user_input % 5 != 0 or user_input <= 0:
            raise Exception("Invalid time.")

        return user_input / 60
    except Exception:
        print("Invalid time.")

def main():
    hours = getHours()
    print(hours)

main()