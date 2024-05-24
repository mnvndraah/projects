line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() 

x = int(position[1])
y = (position[0]).upper()

if x == 1:
    if y == "A":
        line1[0] = "X"
    elif y == "B":
        line1[1] = "X"
    elif y == "C":
        line1[2] = "X"
elif x == 2:
    if y == "A":
        line2[0] = "X"
    elif y == "B":
        line2[1] = "X"
    elif y == "C":
        line2[2] = "X"
elif x == 3:
    if y == "A":
        line3[0] = "X"
    elif y == "B":
        line3[1] = "X"
    elif y == "C":
        line3[2] = "X"

print(f"{line1}\n{line2}\n{line3}")