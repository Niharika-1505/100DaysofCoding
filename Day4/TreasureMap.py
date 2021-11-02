# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
nestedList = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter the digit as column followed by row")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

innerListPosition = round(int(position) / 10)
outerListPosition = int(position) % 10
nestedList[outerListPosition - 1][innerListPosition - 1] = "😍"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
