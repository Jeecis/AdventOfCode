# wget -O input.txt -U "Custom shell script by jekabs.cudars@gmail.com" --no-cookies --header "Cookie: session=53616c7465645f5fd4d5f9896842c27642ec77749b6f71c0d1c8ed0f46e80190c9a9dee840e840683cf2cb734dac727d8c1c7acb5d2305e1670f9d7eea92d18d" https://adventofcode.com/2024/day/2/input

def prepareInput():
    with open("input.txt", "r") as file:
        sum=0
        for line in file:
            strArr=line.split(" ")
            numArr=[]
            for i in range(len(strArr)):
                numArr.append(int(strArr[i]))

            compatibilityIndex = checkCompatibility(numArr[1:])
            if compatibilityIndex==1:
                sum += 1
                print(numArr)
                continue

            compatibilityIndex = checkCompatibility(numArr[:-1])

            if compatibilityIndex==1:
                print(numArr)
                sum += 1
                continue

            compatibilityIndex = checkCompatibility(numArr)

            if compatibilityIndex>-1:
                print(numArr)
                sum += 1


    print(sum)

def checkCompatibility(array):
    increasing = None
    badLevel=False
    previous = None

    for num in array:
        if previous is None:
            previous = num
            continue

        diff= previous-num

        if increasing is None:

            if diff<0 and diff>-4:
                increasing=True
            elif diff>0 and diff<4:
                increasing=False
            else:
                if badLevel:
                    return -1
                badLevel = True

        elif increasing:
            if diff>0 and diff<4:
                if badLevel:
                    return -1
                badLevel = True
                continue
            previous=num
        else:
            if diff<0 and diff>-4:
                if badLevel:
                    return -1
                badLevel=True
                continue
            previous = num

    if badLevel:
        return 0

    return 1

prepareInput()