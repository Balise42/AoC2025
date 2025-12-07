def main():
    grid = [x.strip() for x in open('data/day07.txt').readlines()]
    start = grid[0].find('S')
    beams = {start}

    splits = 0
    timelines = { start: 1 }
    for y in range(0, len(grid)):
        nextbeams = beams.copy()
        nextTimelines = {}
        for x in beams:
            if (grid[y][x] == '^'):
                splits += 1
                nextbeams.remove(x)
                if (x < len(grid[y]) - 1):
                    nextbeams.add(x+1)
                    nextTimelines[x+1] = (nextTimelines[x+1] if x+1 in nextTimelines else 0) + timelines[x]
                if (x > 0):
                    nextbeams.add(x-1)
                    nextTimelines[x-1] = (nextTimelines[x-1] if x-1 in nextTimelines else 0) + timelines[x]
            else:
                nextTimelines[x] = (nextTimelines[x] if x in nextTimelines else 0) + timelines[x]
        beams = nextbeams
        timelines = nextTimelines
    print(splits)
    print(sum(timelines.values()))

main()