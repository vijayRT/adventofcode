import Levenshtein
def Part1():
    def generatecountdict():
        countdict = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            countdict[letter] = 0
        return countdict

    twocount = set()
    threecount = set()

    with open("day2codes.txt", "r") as f:
        codes = f.readlines()
        for code in codes:
            countdict = generatecountdict()
            for letter in code[:-1]:
                countdict[letter] += 1
            for key in countdict:
                if countdict[key] == 2:
                    twocount.add(code)
                if countdict[key] == 3:
                    threecount.add(code)

    return len(twocount) * len(threecount)

def Part2():
    with open("day2codes.txt", "r") as f:
        codes = f.readlines()
        for i in range(len(codes) - 1):
            for j in range(i+1, len(codes)):
                if Levenshtein.distance(codes[i], codes[j]) == 1:
                    return codes[i], codes[j]
part1answer = Part1()
part2code1, part2code2 = Part2()
print(part2code1, part2code2)