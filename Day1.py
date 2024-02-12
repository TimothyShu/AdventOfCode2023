from typing import Dict

wordToNum: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def FindFirst(line:str) -> list[int]:
    stringslice = ""
    for index, num in enumerate(line):
        stringslice += num
        for (word, value) in wordToNum.items():
            if (word in stringslice):
                return [value, index]
        if (num.isnumeric()==False):
            continue
        
        return [int(num), index]
    
def FindLast(line:str, index:int) -> int:
    stringslice = ""
    count = len(line) - 1
    while (count > index):
        stringslice = line[count:]
        for (word, value) in wordToNum.items():
            if (word in stringslice):
                return value
        if line[count].isnumeric()==False:
            count -= 1
            continue
        return int(line[count])
    return 0


with open("Day1Input.txt", "r") as file:
    numSum = 0
    for line in file:
        # Process each line here
        line = line.strip()  # Example: Print each line
        startnum = FindFirst(line)
        endnum = FindLast(line, startnum[1])
        if (endnum == 0):
            endnum = startnum[0]
        numSum += startnum[0] * 10 + endnum
    print(numSum)