
def prepare_input():
    antennas={}
    graph = []
    with open("input.txt") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line=[]
            strippedLine=lines[i].strip()
            for j in range(len(strippedLine)):
                element =lines[i][j]
                if element != ".":
                    if element not in antennas:
                        antennas[element]=[(j,i)]
                    else:
                        antennas[element].append((j,i))
                line.append(element)
            graph.append(line)
    return graph, antennas

def antidoteValidity(graph, antidotes):
    sum =0
    xleng= len(graph[0])
    yleng= len(graph)
    for antidote in antidotes:
        x=antidote[0]
        y=antidote[1]
        if x>= xleng or x<0:
            continue
        if y>= yleng or y<0:
            continue

        if graph[y][x] == "#":
            continue
        graph[y][x]="#"
        sum+=1

    return graph, sum

def isOutOfBounds(graph, antidote):
    xleng= len(graph[0])
    yleng= len(graph)
    x = antidote[0]
    y = antidote[1]
    if x >= xleng or x < 0:
        return graph, 1
    if y >= yleng or y < 0:
        return graph, 1

    if graph[y][x] != ".":
        return graph, 0

    graph[y][x] = "#"
    return graph, -1

def antidoteValidityLong(graph, firstCor, secCor, diff):
    sum =0

    antidoteFirst= firstCor
    antidoteSec=secCor
    ok=0
    while ok !=1:
        if ok==-1:
            sum +=1
        antidoteFirst = (antidoteFirst[0]+diff[0], antidoteFirst[1]+diff[1])
        graph, ok= isOutOfBounds(graph, antidoteFirst)

    ok=0
    while ok !=1:
        if ok==-1:
            sum +=1
        antidoteSec = (antidoteSec[0]-diff[0], antidoteSec[1]-diff[1])
        graph, ok= isOutOfBounds(graph, antidoteSec)

    return graph, sum

def checkAntidotes(graph, coordinates):
    sum=0
    for i in range(len(coordinates)):
        firstCoordinate=coordinates[i]
        for j in range(i+1, len(coordinates)):
            secCoordinate = coordinates[j]
            difference =(firstCoordinate[0]-secCoordinate[0], firstCoordinate[1]-secCoordinate[1])

            # antidote1 =(firstCoordinate[0]+difference[0], firstCoordinate[1]+difference[1])
            # antidote2=(secCoordinate[0]-difference[0], secCoordinate[1]-difference[1])
            #
            # graph, correctSum=antidoteValidity(graph, [antidote1,antidote2])
            graph, correctSum = antidoteValidityLong(graph, firstCoordinate, secCoordinate, difference)
            sum+= correctSum

    return graph, sum



def setAntidotes(graph, antennas):
    total=0
    for key in antennas.keys():
        coordinates = antennas[key]
        total += len(antennas[key])
        graph, sum = checkAntidotes(graph, coordinates)
        total+= sum
    return graph, total



graph, antennas =prepare_input()
# print(antennas)
graph, total = setAntidotes(graph, antennas)
print(total)
for entry in graph:
    print(entry)

