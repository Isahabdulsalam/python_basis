row1 = ['😀','😀,','😀']
row2 = ['😀','😀,','😀']
row3 = ['😀','😀,','😀']
maxtrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("Enter the position yoi want to hide your money: ")
#32
row_number=int(position[0])
column_number=int(position[1])
row_selected=maxtrix[row_number-1]
row_selected[column_number-1]= '👏'
print(f"{row1}\n{row2}\n{row3}")
