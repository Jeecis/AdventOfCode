# wget -O input.txt -U "Custom shell script by jekabs.cudars@gmail.com" --no-cookies --header "Cookie: session=53616c7465645f5fd4d5f9896842c27642ec77749b6f71c0d1c8ed0f46e80190c9a9dee840e840683cf2cb734dac727d8c1c7acb5d2305e1670f9d7eea92d18d" https://adventofcode.com/2024/day/3/input
import re
def regexAnalyze():
    sum=0
    with open("input.txt", "r") as file:
        text = "".join(file.readlines())
        list = re.findall(r"mul\([1-9]?[0-9]{0,2},[1-9]?[0-9]{0,2}\)|do\(\)|don't\(\)", text)
        print(list)

        enabled=True
        for i in range(len(list)):
            if list[i] == "don't()":
                enabled=False
            elif list[i] == "do()":
                enabled=True
            elif enabled:
                match = re.match(r"mul\((\d+),(\d+)\)", list[i])
                num1, num2 = map(int, match.groups())  # Convert both numbers to integers
                result = num1 * num2  # Multiply the numbers
                sum+=result

        print(sum)

regexAnalyze()