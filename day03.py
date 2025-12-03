def main():
    f = open('data/day03.txt')
    s = 0
    for line in f:
        line = line.strip()
        pos = -1
        max = -1
        jolt = 0
        bat = 12

        for j in range(bat - 1, -1, -1):
            curs = pos + 1
            max = -1
            for i in range(curs, len(line) - j):
                digit = int(line[i])
                if digit > max:
                    max = digit
                    pos = i
            jolt = jolt * 10 + max
        s += jolt
    print(s) 

main()
