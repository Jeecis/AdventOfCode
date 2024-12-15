# wget -O input.txt -U "Custom shell script by jekabs.cudars@gmail.com" --no-cookies --header "Cookie: session=53616c7465645f5fd4d5f9896842c27642ec77749b6f71c0d1c8ed0f46e80190c9a9dee840e840683cf2cb734dac727d8c1c7acb5d2305e1670f9d7eea92d18d" https://adventofcode.com/2024/day/9/input
def prepare_input_part_1():
    memoryArray = []
    with open("input.txt") as file:
        line=file.readlines()[0]

    isByte=True
    id=0
    for elem in line:
        if elem=="\n":
            break
        if isByte:
            count=int(elem)
            for i in range(count):
                memoryArray.append(id)
            id+=1
            isByte=False
        else:
            isByte=True
            count=int(elem)
            for i in range(count):
                memoryArray.append(-1) # we append -1 to store only the same types of elements in the array

    return memoryArray

def loop_back_part_1(memoryArray):
    startPointer=0
    endPointer = len(memoryArray)-1
    i=0
    while(i<len(memoryArray)):
        startElem = memoryArray[startPointer]
        endElem = memoryArray[endPointer]
        if startElem[1] != -1:
            startPointer+=1
            i+=1
            continue


        if endElem[1] ==-1:
            endPointer-=1
            i += 1
            continue

        memoryArray[startPointer]=memoryArray[endPointer]
        memoryArray[endPointer] =-1
        startPointer+=1
        endPointer-=1
        i+=2 # to increment for the changes an so the loop terminates at O(n) time

    return memoryArray

def check_sum_part_1(memoryArray):
    sum=0
    for i in range(len(memoryArray)):
        elem=memoryArray[i]
        if elem ==-1:
            return sum
        sum+=i*elem
    return sum

def loop_back_part_2(memoryArray):
    currentVal=memoryArray[len(memoryArray)-1]
    blockSize=0
    visited=set()
    for i in range(len(memoryArray)-1,0,-1):
        elem=memoryArray[i]
        if elem==-1 or elem!=currentVal:

            if not currentVal in visited:
                memoryArray=find_free_spot(memoryArray, blockSize, currentVal, i)
                visited.add(currentVal)


            currentVal = elem
            if elem!=-1:
                blockSize = 1
            else:
                blockSize=0
            continue

        currentVal=elem
        blockSize +=1

    return memoryArray

def find_free_spot(memoryArray, length, current_val, index):
    blockSize=0
    for i in range(0,index, 1):
        elem=memoryArray[i]
        if elem==-1:
            blockSize +=1
            if blockSize == length:
                for j in range(length):
                    memoryArray[i-j]=current_val
                    memoryArray[index+j+1]=-1
                return memoryArray
        else:
            blockSize=0


    return memoryArray


def check_sum_part_2(memoryArray):
    sum=0
    for i in range(len(memoryArray)):
        elem=memoryArray[i]
        if elem ==-1:
            continue
        sum+=i*elem
    return sum

# part 1
memoryArray = prepare_input_part_1()
memoryArray = loop_back_part_1(memoryArray)
sum =check_sum_part_1(memoryArray)
print(sum)

# part 2
memoryArray = prepare_input_part_1()
memoryArray = loop_back_part_2(memoryArray)
sum = check_sum_part_2(memoryArray)
print(memoryArray)
print(sum)
