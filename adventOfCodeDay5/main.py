
class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node]={}

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        self.adjacency_list[from_node][to_node] = 1
        self.adjacency_list[to_node][from_node] = 0

    def get_neighbours(self, node):
        return self.adjacency_list.get(node,[])

    def __str__(self):
        return str(self.adjacency_list)

def prepare_input():
    graph = Graph()
    updates=[]
    with open("input.txt") as file:

        areRules =True
        for line in file.readlines():
            line = line.strip()
            if line != "" and areRules:
                nums = line.split("|")
                graph.add_edge(nums[0], nums[1])
                continue
            elif line=="":
                areRules=False
            else:
                nums = line.split(",")
                updates.append(nums)

    return graph, updates

def checkUpdate(graph, update):
    for i in range(len(update)):
        adjacentNodesForI = graph.adjacency_list[update[i]]
        for j in range(i+1,len(update)):
            relationship = adjacentNodesForI[update[j]]
            if relationship==0:
                return False
    return True

def getSumCorrect(graph, updates):
    totalSum=0
    for update in updates:
        isCorrect = checkUpdate(graph, update)
        if isCorrect:
            middle =int((len(update)/2))
            num =int(update[middle])
            totalSum += num

    return totalSum

def orderUpdate(graph, elements):
    needOrderArray = list(elements)
    needOrderArray.reverse()

    i=len(needOrderArray)-1
    while i> 0:
        element = needOrderArray[i]
        adjecancyList = graph.adjacency_list.get(element, [])
        restart=False
        for j in range(i-1, -1, -1):
            if adjecancyList[needOrderArray[j]]==0:
                incorrectElement =needOrderArray.pop(j)
                needOrderArray.append(incorrectElement)
                restart =True
        if restart:
            i = len(needOrderArray)
        i-=1

    needOrderArray.reverse()

    return needOrderArray


def getSumIncorrect(graph, updates):
    totalSum=0
    for update in updates:
        isCorrect = checkUpdate(graph, update)
        if not isCorrect:
            orderedUpdate =orderUpdate(graph, update)
            middle =int((len(orderedUpdate)/2))
            num =int(orderedUpdate[middle])
            totalSum += num

    return totalSum

graph, updates =prepare_input()

# totalSum = getSumCorrect(graph, updates)
totalSum = getSumIncorrect(graph, updates)
print(totalSum)

