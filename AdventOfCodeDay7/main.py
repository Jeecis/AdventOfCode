from itertools import product
def prepare_input():
    expressions=[]
    with open("input.txt") as file:
        for line in file.readlines():
            split= line.split(":")
            resultingNum=int(split[0])

            numberSplit =split[1].strip().split(" ")
            numbers =[resultingNum]
            for num in numberSplit:
                numbers.append(int(num))


            expressions.append(numbers)

    return expressions

def test(expression):
    resultingNum= expression[0]
    numbers = expression[1:]
    length= len(numbers)
    signLen = length-1
    max_count=pow(2, length-1)

    counter = 0

    while counter <= max_count:
        signs = ''.join('*' if bit == '0' else '+' for bit in format(counter, f'0{signLen}b'))
        res=numbers[0]
        for i in range(signLen):
            if signs[i]=="+":
                res+=numbers[i+1]
            else:
                res *= numbers[i+1]
        if res==resultingNum:
            return True
        counter += 1
    return False

def test2(expression):
    resultingNum= expression[0]
    numbers = expression[1:]
    length= len(numbers)
    signLen = length-1

    symbols = ['*', '+', '/']
    combinations = product(symbols, repeat=signLen)

    counter = 0

    for combination in combinations:
        res=numbers[0]
        signs=''.join(combination)
        for i in range(len(signs)):
            if signs[i]=="+":
                res+=numbers[i+1]
            elif signs[i]=="*":
                res *= numbers[i+1]
            elif signs[i]=="/":
                res = int(str(res)+str(numbers[i+1]))
        if res==resultingNum:
            return True
        counter += 1
    return False

def checkExpressions(expressions):
    sum=0
    for expression in expressions:
        if test(expression):
            sum+= expression[0]
    return sum

def checkExpressions2(expressions):
    sum=0
    for expression in expressions:
        if test2(expression):
            sum+= expression[0]
    return sum


expressions=prepare_input()

# correctExpressionSum = checkExpressions(expressions)
# print(correctExpressionSum)

correctExpressionSum2 = checkExpressions2(expressions)
print(correctExpressionSum2)