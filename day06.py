import operator
import functools

def main():
    file = open('data/day06.txt', 'r')
    lines = []
    lines2 = []
    for line in file.readlines():
        if line[0] == '+' or line[0] == '*':
            operators = [operator.mul if x == '*' else operator.add for x in line.split()]
        else:
            lines.append([int(x) for x in line.split()])
            lines2.append(line)
    
    res = 0
    for i in range(len(lines[0])):
        res += functools.reduce(operators[i], [line[i] for line in lines])
    print(res)

    j = len(operators) - 1
    arr = []
    res = 0
    for i in range(len(lines2[0])-1, -2, -1):
        num = 0
        for line in lines2:
            if (line[i].isnumeric()):
                num = num*10 + int(line[i])
        if num != 0:
            arr.append(num)
        else:
            if len(arr) > 0:
                res += functools.reduce(operators[j], arr)
                arr = []
                j -= 1
    print(res)

main()

