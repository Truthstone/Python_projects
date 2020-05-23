values = [" "] * 9
chance = 0
print("---------")
for i in range(0,9,3):
    print("|", end=" ")
    for j in range(0,3):
        print(values[i+j], end=" ")
    print("|")
print("---------")
xwin = 0
owin = 0
while True:
    x, y = input("Enter the coordinates: ").split()
    if len(x) < 2 and len(y) < 2 and 48 <= ord(x) <= 57 and 48 <= ord(y) <= 57:
        x = int(x)
        y = int(y)
        if 1 <= x <= 3 and 1 <= y <= 3:
            if values[(abs(y - 3)) * 3 + x - 1] == "X" or values[(abs(y - 3)) * 3 + x - 1] == "O":
                print("This cell is occupied! Choose another one!" )
            else:
                if chance %2 == 0:
                    values[(abs(y - 3)) * 3 + x - 1] = "X"
                else:
                    values[(abs(y - 3)) * 3 + x - 1] = "O"
                print("---------")
                for i in range(0,9,3):
                    print("|", end=" ")
                    for j in range(0,3):
                        print(values[i+j], end=" ")
                    print("|")
                print("---------")
                if "".join([values[0], values[1], values[2]]) == "XXX" or "".join([values[3], values[4], values[5]]) == "XXX" or "".join([values[6], values[7], values[8]]) == "XXX" or "".join([values[0], values[3], values[6]]) == "XXX" or "".join([values[1], values[4], values[7]]) == "XXX" or "".join([values[2], values[5], values[8]]) == "XXX" or "".join([values[0], values[4], values[8]]) == "XXX" or "".join([values[2], values[4], values[6]]) == "XXX" :
                    xwin = 1
                if "".join([values[0], values[1], values[2]]) == "OOO" or "".join([values[3], values[4], values[5]]) == "OOO" or "".join([values[6], values[7], values[8]]) == "OOO" or "".join([values[0], values[3], values[6]]) == "OOO" or "".join([values[1], values[4], values[7]]) == "OOO" or "".join([values[2], values[5], values[8]]) == "OOO" or "".join([values[0], values[4], values[8]]) == "OOO" or "".join([values[2], values[4], values[6]]) == "OOO" :
                    owin = 1
                if xwin:
                    print("X wins")
                    break
                elif owin:
                    print("O wins")
                    break
                elif values.count(" ") == 0:
                    print("Draw")
                    break
                chance += 1
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
