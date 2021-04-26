import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\Landscape.xlsx"
df = pd.read_excel(file)  # reading file


def treehit(rowvalue: str, position: int) -> bool:
    treehit = False
    positionmodulus = position % 31
    print("Position: "+str(positionmodulus))
    if rowvalue[positionmodulus-1] == "#":
        treehit = True
        print("hit")
        return treehit
    else:
        print("tree not hit")

rowCount = 0
hit_counter = 0
for ind, row1 in df.iterrows():
    print(row1[0])
    if treehit(row1[0], (1+rowCount*3)):
        hit_counter = hit_counter + 1
        rowCount = rowCount + 1
    else:
        rowCount = rowCount + 1

print(hit_counter)



