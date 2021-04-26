import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\Passwords.xlsx"
df = pd.read_excel(file)  # reading file

counter = 0

# gets the letter
def getletter(entry: str) -> str:
    condition = entry.split(":")[0]
    letter = condition.split(" ")[1]
    return letter


# gets the password
def getpassword(entry: str) -> str:
    password = entry.split(":")[1]
    return password


# counts how many times the letter is in the word
def validate(interval, letter: str, password: str) -> bool:
    validatebool = False
    counter = 1
    for i in password:
        if counter == interval[0] or counter == interval[1]:
            if i == letter:
                if validatebool == False:
                    validatebool = True
                    counter = counter + 1
                else:
                    validatebool = False
                    counter = counter + 1
            else:
                counter = counter + 1
                continue
        else:
            counter = counter + 1
            continue

    return validatebool



# gets the range
def getinterval(entry: str):
    condition = entry.split(" ")[0]
    numbers = condition.split("-")
    interval = [int(numbers[0]), int(numbers[1])]
    return interval


# true if number is in range
def numinrange(lettercount: int, interval):
    if lettercount >= interval[0] and lettercount <= interval[1]:
        return True
    else:
        return False

outcomeCounter = 0

for ind, row1 in df.iterrows():
    if validate(getinterval(row1[0]), getletter(row1[0]), getpassword(row1[0]).strip()):
        outcomeCounter = outcomeCounter + 1
        print(row1[0])
        print(str(getinterval(row1[0])))
        print(str(getletter(row1[0])))
        print(str(getpassword(row1[0])))
    else:
        continue

print(outcomeCounter)


