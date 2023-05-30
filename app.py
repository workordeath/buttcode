from datetime import date

def displayMenu():
    print("main menu")
    print("1. Input Payroll Data")
    print("2. Show Payroll Data")
    print("3. quit")

def grabInput():
    userInput = int(input(">> "))
    return userInput

def sendToFunctions(userinput):
    if userinput == 1:
        print("loading input payroll data")
        appendToFile()
    elif userinput == 2:
        print("loading show payroll data")
        outputFile()
    else:
        print("input not valid")

def getCurrentIndex():
    indexFile = open("index.txt", 'r')
    keyIndex = indexFile.read()
    indexFile.close()

    return keyIndex

def updateFileIndex(previousIndex):
    updatedIndex = int(previousIndex) + 1
    indexFile = open("index.txt", 'w')
    indexFile.write(str(updatedIndex))
    indexFile.close()

def appendToFile():
    currentIndex = getCurrentIndex()
    print("enter your payment")
    payment = float(input(">> "))
    print("enter the time that you worked")
    workduration = float(input(">> "))

    dataFile = open("data.txt", 'a')
    ## creates a new row of data in the file
    dataFile.write(f"{currentIndex},knack,{payment:.2f},{workduration:.2f},{date.today()}")
    dataFile.write("\n")
    dataFile.close()

    updateFileIndex(currentIndex)

def outputFile():
    dataFile = open("data.txt", 'r')
    totalEarnings = 0.0
    for line in dataFile:
        row = line.strip().split(',')
        totalEarnings += float(row[2])

        for field in row:
            print(f"{field} ", end='')
        print()
        row.clear()
    dataFile.close()
    print(f"GROSS EARNINGS ${totalEarnings:.2f}")
    print(f"NET EARNINGS ${totalEarnings - (totalEarnings * 0.153):.2f}")
    print(f"TAXES DUE ${totalEarnings * 0.153:.2f}")

def main():
    while True:
        displayMenu()
        userInput = grabInput()
        if userInput == 3:
            break
        sendToFunctions(userInput)

main()