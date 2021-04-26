import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\Numbers.xlsx"
df = pd.read_excel(file)  # reading file


# loop through to get first number
for ind, row1 in df.iterrows():
    currentNumber = int(row1[0])
    # loop through to add second number
    for ind, row2 in df.iterrows():
        tempNumber1 = int(row2[0])
        if currentNumber + tempNumber1 < 2020:
            # if less than 2020 then loop through to add third number
            for ind, row3 in df.iterrows():
                tempNumber2 = int(row3[0])
                if (currentNumber + tempNumber1 + tempNumber2) == 2020:
                    print(currentNumber*tempNumber1*tempNumber2)
                    print(currentNumber + tempNumber1 + tempNumber2)
                else:
                    continue
        else:
            continue





