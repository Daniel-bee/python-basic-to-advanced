row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map_ = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position[0])
row = int(position[1])
if col == len(map_):
    col = len(map_) - 1
else:
    col -= 1
if row == len(map_):
     row = len(map_) - 1
else:
    row -= 1

map_[row][col] = "✖"
print(f"{row1}\n{row2}\n{row3}")
