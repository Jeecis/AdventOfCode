#wget -O input.txt -U "Custom shell script by jekabs.cudars@gmail.com" --no-cookies --header "Cookie: session=53616c7465645f5fd4d5f9896842c27642ec77749b6f71c0d1c8ed0f46e80190c9a9dee840e840683cf2cb734dac727d8c1c7acb5d2305e1670f9d7eea92d18d" https://adventofcode.com/2024/day/4/input

def prepare_input():
    with open("input.txt") as file:
        table=[]
        for line in file.readlines():
            symbolArray = list(line)
            table.append(symbolArray)

        return table
def getNeighbours(table, coordinates):
    xLeng = len(table[0])-1
    yLeng =len(table)
    neighbourCoordinates =getNeighbouringCoordinates(coordinates, xLeng, yLeng)
    Ms =[]

    for coordinate in neighbourCoordinates:
        char =table[coordinate[0]][coordinate[1]]
        if char=="M":
            Ms.append(coordinate)



    return Ms

def getNeighbouringCoordinates(coordinates, xLeng, yLeng):
    xValues = [(coordinates[0]-1, "U"), (coordinates[0],"C"), (coordinates[0]+1,"D")]
    yValues = [(coordinates[1]-1, "L"), (coordinates[1],"C"), (coordinates[1]+1, "R")]
    neighbours =[]
    for x in xValues:
        for y in yValues:
            if x[0]<0 or y[0]<0 or x[0]>=xLeng or y[0]>=yLeng or (x[0]==coordinates[0] and y[0]== coordinates[1]):
                continue
            neighbours.append((x[0],y[0], x[1]+y[1]))

    return neighbours

def checkForMAS(Ms, table):
    sum=0
    for m in Ms:
        match(m[2]):
            case "DL":
                mx =m[0]
                my = m[1]
                try:
                    if table[mx+1][my-1]=="A" and table[mx+2][my-2] == "S":
                        sum+=1
                        print([(mx, my), (mx+1, my - 1), (mx+2, my - 2)])
                except IndexError:
                    continue

            case "CL":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx][my-1]=="A" and table[mx][my-2] == "S":
                        sum+=1
                        print([(mx, my), (mx, my-1), (mx, my-2)])
                except IndexError:
                    continue

            case "UL":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx - 1][my - 1]=="A" and table[mx - 2][my - 2] == "S":
                        sum+=1
                        print([(mx, my), (mx - 1, my-1), (mx - 2, my-2)])
                except IndexError:
                    continue

            case "DC":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx+1][my]=="A" and table[mx+2][my] == "S":
                        sum+=1
                        print([(mx,my),(mx+1, my),(mx+2,my)])
                except IndexError:
                    continue
            case "UC":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx-1][my]=="A" and table[mx-2][my] == "S":
                        sum+=1
                        print([(mx, my), (mx-1, my), (mx-2, my)])
                except IndexError:
                    continue
            case "DR":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx + 1][my + 1]=="A" and table[mx + 2][my + 2] == "S":
                        sum+=1
                        print([(mx, my), (mx + 1, my + 1), (mx + 2, my + 2)])
                except IndexError:
                    continue
            case "CR":
                mx = m[0]
                my = m[1]

                try:
                    if table[mx][my+1]=="A" and table[mx][my + 2] == "S":
                        sum+=1
                        print([(mx, my), (mx, my+1), (mx , my +2)])
                except IndexError:
                    continue
            case "UR":
                mx = m[0]
                my = m[1]
                try:
                    if table[mx -1][my + 1]=="A" and table[mx - 2][my + 2]== "S":
                        sum+=1
                        print([(mx, my), (mx - 1, my + 1), (mx - 2, my + 2)])
                except IndexError:
                    continue
    return sum

def getXmasBig(table):
    sum=0
    for i in range(len(table)):
        for j in range(len(table)):
            char = table[i][j]
            if char =="M":
                try:
                    if table[i][j+2]=="M" and table[i+1][j+1]=="A" and table[i+2][j+2]=="S" and table[i+2][j]=="S":
                        sum +=1
                    elif table[i][j+2]=="S" and table[i+1][j+1]=="A" and table[i+2][j+2]=="S" and table[i+2][j]=="M":
                        sum +=1
                except IndexError:
                    continue
            if char == "S":
                try:
                    if table[i][j + 2] == "S" and table[i + 1][j + 1] == "A" and table[i + 2][j + 2] == "M" and \
                            table[i + 2][j] == "M":
                        sum += 1
                    elif table[i][j + 2] == "M" and table[i + 1][j + 1] == "A" and table[i + 2][j + 2] == "M" and \
                            table[i + 2][j] == "S":
                        sum += 1
                except IndexError:
                    continue

    print(sum)

def getXmasSmall(table):
    sum=0
    for i in range(len(table)):
        for j in range(len(table)):
            char = table[i][j]
            if char =="X":
                Ms = getNeighbours(table, (i,j))
                if len(Ms)>0:
                    print("For:")
                    print((i,j))
                    print(Ms)
                    res = checkForMAS(Ms, table)
                    sum +=res
    print(sum)

table = prepare_input()

# getXmasSmall(table)

getXmasBig(table)

