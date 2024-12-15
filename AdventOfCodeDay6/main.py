# wget -O input.txt -U "Custom shell script by jekabs.cudars@gmail.com" --no-cookies --header "Cookie: session=53616c7465645f5fd4d5f9896842c27642ec77749b6f71c0d1c8ed0f46e80190c9a9dee840e840683cf2cb734dac727d8c1c7acb5d2305e1670f9d7eea92d18d" https://adventofcode.com/2024/day/6/input
import copy
def prepare_input():
    grid =[]
    start=()
    obstacles =[]
    with open("input.txt") as file:
        lines =file.readlines()

        for i in range(len(lines)):
            line = lines[i].strip()
            elements = list(line)
            for j in range(len(elements)):
                element =elements[j]
                if element =="#":
                    obstacles.append((j,i))
                elif element=="^":
                    start=(j,i)

            grid.append(elements)


    return grid, obstacles, start

def checkOutside(position, xleng, yleng):
    if position[0]<0 or position[0]>=xleng:
        return False
    elif position[1]<0 or position[1]>=yleng:
        return False

    return True

def findPath(grid, start):
    direction = "U"
    xLeng=len(grid[0])
    yLeng=len(grid[1])
    nextPos = (start[0], start[1]+1)
    total =0
    notSafe = checkOutside(nextPos, xLeng, yLeng)
    xCoordinates=[]
    while notSafe:
        if nextPos[1]==9:
            print("yee")
        match(direction):
            case "U":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="R"
                    nextPos = (nextPos[0] + 1, nextPos[1]+1)
                elif element == "X":
                    nextPos =(nextPos[0], nextPos[1]-1)
                else:
                    grid[nextPos[1]][nextPos[0]] = "X"
                    xCoordinates.append(nextPos)
                    nextPos = (nextPos[0], nextPos[1] - 1)
                    total+=1
            case "R":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="D"
                    nextPos = (nextPos[0]-1, nextPos[1]+1)
                elif element == "X":
                    nextPos =(nextPos[0]+1, nextPos[1])
                else:
                    grid[nextPos[1]][nextPos[0]] = "X"
                    xCoordinates.append(nextPos)
                    nextPos =(nextPos[0]+1, nextPos[1])
                    total += 1
            case "D":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="L"
                    nextPos = (nextPos[0]-1, nextPos[1]-1)
                elif element == "X":
                    nextPos =(nextPos[0], nextPos[1]+1)
                else:
                    grid[nextPos[1]][nextPos[0]] = "X"
                    xCoordinates.append(nextPos)
                    nextPos = (nextPos[0], nextPos[1] + 1)
                    total += 1
            case "L":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction = "U"
                    nextPos = (nextPos[0]+1, nextPos[1]-1)
                elif element == "X":
                    nextPos =(nextPos[0]-1, nextPos[1])
                else:
                    grid[nextPos[1]][nextPos[0]] = "X"
                    xCoordinates.append(nextPos)
                    nextPos = (nextPos[0] - 1, nextPos[1])
                    total += 1
        notSafe=checkOutside(nextPos, xLeng, yLeng)

    return grid, total, xCoordinates

def test(grid,start, coordinate):
    grid[coordinate[1]][coordinate[0]] = "#"

    direction = "U"
    xLeng=len(grid[0])
    yLeng=len(grid[1])
    nextPos = (start[0], start[1]+1)
    notSafe = checkOutside(nextPos, xLeng, yLeng)
    while notSafe:
        match(direction):
            case "U":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="R"
                    nextPos = (nextPos[0] + 1, nextPos[1]+1)
                elif element == "^":
                    return True
                else:
                    grid[nextPos[1]][nextPos[0]] = "^"
                    nextPos = (nextPos[0], nextPos[1] - 1)
            case "R":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="D"
                    nextPos = (nextPos[0]-1, nextPos[1]+1)
                elif element == ">":
                    return True
                else:
                    grid[nextPos[1]][nextPos[0]] = ">"
                    nextPos =(nextPos[0]+1, nextPos[1])
            case "D":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction="L"
                    nextPos = (nextPos[0]-1, nextPos[1]-1)
                elif element == "v":
                    return True
                else:
                    grid[nextPos[1]][nextPos[0]] = "v"
                    nextPos = (nextPos[0], nextPos[1] + 1)
            case "L":
                element =grid[nextPos[1]][nextPos[0]]
                if element=="#":
                    direction = "U"
                    nextPos = (nextPos[0]+1, nextPos[1]-1)
                elif element == "<":
                    return True
                else:
                    grid[nextPos[1]][nextPos[0]] = "<"
                    nextPos = (nextPos[0]-1, nextPos[1])
        notSafe=checkOutside(nextPos, xLeng, yLeng)

    return False


def checkLoops(grid, start, xCoordinates):
    total =0
    leng=len(xCoordinates)
    for i in range(leng):
        print(xCoordinates[i])
        gridCopy = copy.deepcopy(grid)

        if test(gridCopy,start, xCoordinates[i]):
            total+=1
        print("iteration No. "+ str(i)+ " total: "+str(total))

    return total

import time

startTime = time.time()
# Code block to time

grid, obstacles, start = prepare_input()
grid, total, xCoordinates=findPath(grid, start)

loopedObstacles = checkLoops(grid, start, xCoordinates)
print("Total loops: "+str(loopedObstacles))

grid[start[1]][start[0]]="^"

with open("res.txt","w") as file:
    for row in grid:
        for elem in row:
            file.write(elem)
        file.write("\n")

end = time.time()

print(f"Execution time: {end - startTime:.5f} seconds")

