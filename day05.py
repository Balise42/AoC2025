def main():
    f = open('data/day05.txt', 'r')
    inRanges = True
    intervals = []
    fresh = 0
    for line in f.readlines():
        if line.strip() == '':
            inRanges = False
            continue
        if inRanges:
            intervals.append([int(x) for x in line.strip().split('-')])
        else:
            id = int(line.strip())
            for interval in intervals:
                if id >= interval[0] and id <= interval[1]:
                    fresh += 1
                    break
    print(fresh)

    lefts = [x[0] for x in intervals]
    lefts.sort()
    rights = [x[1] for x in intervals]
    rights.sort()
    
    opened = 0
    merged = []
    a = -1

    while len(lefts) > 0 and len(rights) > 0:
        if lefts[0] < rights[0]:
            opened += 1
            if a == -1:
                a = lefts[0]
            lefts = lefts[1:]
        elif rights[0] < lefts[0]:
            opened -=1
            if opened == 0:
                merged.append([a, rights[0]])
                a = -1
            rights = rights[1:]  
        else:
            if (a == -1):
                merged.append([lefts[0],lefts[0]])
            lefts = lefts[1:]
            rights = rights[1:]

    if (len(rights) > 0):
        merged.append([a, rights[-1]])


    todel = 0
    for i in range(1, len(merged) - 1):
        if merged[i][0] == merged[i][1] and (merged[i][0] == merged[i-1][1] or merged[i][0] == merged[i+1][0]):
            todel += 1

    print(sum([x[1] - x[0] + 1 for x in merged]) - todel)
main()