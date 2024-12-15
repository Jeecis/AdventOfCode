import requests
def prepareInput():
    with open("input.txt", "r") as file:
        leftArray=[]
        rightArray = []
        for line in file:
            nums=line.split("   ")
            leftArray.append(int(nums[0]))
            rightArray.append(int(nums[1]))

    return leftArray, rightArray



def calculate(leftArray, rightArray):
    sortedLeft= sorted(leftArray)
    sortedRight = sorted(rightArray)
    sum=0
    for i in range(len(leftArray)):
        sum+=abs(int(sortedLeft[i])-int(sortedRight[i]))
    print(sum)
    return sortedLeft, sortedRight

def similarity(l, r):
    lp=0
    rp=0
    sum=0

    while lp <len(l) and rp<len(r):
        if lp!=0 and l[lp]==l[lp-1]:
            lp += 1
            continue

        if l[lp]<r[rp]:
            lp += 1
            continue

        if l[lp]>r[rp]:
            lp-=1
            rp+=1

        if rp >= len(r):
            break

        if l[lp]==r[rp]:
            multiple =1
            rp+=1
            while l[lp]==r[rp]:
                rp += 1
                multiple+=1
            sum+=multiple*l[lp]
        lp+=1

    print(sum)


l, r =prepareInput()
l, r=calculate(l,r)
similarity(l,r)