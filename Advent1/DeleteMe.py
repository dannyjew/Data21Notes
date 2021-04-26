import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\DeleteMe.xlsx"
df = pd.read_excel(file)  # reading file

for ind, row in df.iterrows():
    print(row[0])