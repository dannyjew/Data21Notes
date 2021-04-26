import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\Passwords.xlsx"
df = pd.read_excel(file)  # reading file

counter = 0

# gets the letter
def getletter(entry: str) -> str:
    condition = entry.split(":")[0]
    letter = condition.split(" ")[1]
    return letter


# gets the letter
def getpassword(entry: str) -> str:
    password = entry.split(":")[1]
    return password


# counts how many times the letter is in the word
def countletter(letter: str, password: str) -> int:
    counter = 0
    for i in password:
        if i == letter:
            counter = counter + 1
        else:
            continue
    return counter

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


for ind, row1 in df.iterrows():
    print(row1[0])
    letter = getletter(str(row1[0]))
    password = getpassword(str(row1[0]))
    interval = getinterval(str(row1[0]))
    lettercount = countletter(letter, password)
    print(interval)
    if numinrange(lettercount, interval):
        counter = counter + 1
    else:
        continue

print(counter)