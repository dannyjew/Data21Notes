import pandas as pd

file = "C:\\Users\\DJew\\Documents\\Learning\\Python\\Data21Notes\\Advent1\\Landscape.xlsx"
df = pd.read_excel(file)  # reading file


def treehit(rowvalue: str, position: int) -> bool:
    treehit = False
    positionmodulus = position % 31
    # print("position: "+str(positionmodulus))
    if rowvalue[positionmodulus] == "#":
        treehit = True
        return treehit
    else:
        return treehit

def outcome(across: int, down: int):
    rowCount = 0
    multipliedRowCount = 0
    hit_counter = 0
    for ind, row1 in df.iterrows():
        # print(row1[0])
        # print(str(ind))
        if (rowCount) % down == 0:
            if treehit(row1[0], (multipliedRowCount*across)):
                hit_counter = hit_counter + 1
                multipliedRowCount = multipliedRowCount + 1
                rowCount = rowCount + 1
                # print("Hit Counter: "+str(hit_counter))
            else:
                rowCount = rowCount + 1
                multipliedRowCount = multipliedRowCount + 1
        else:
            rowCount = rowCount + 1

    return(hit_counter)


gradients = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

total = 1

for i in gradients:
    total = total*outcome(i[0], i[1])
    print(str(i[0])+" "+str(i[1])+" "+str(outcome(i[0], i[1])))

print(total)
