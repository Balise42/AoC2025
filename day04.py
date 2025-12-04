def main():
    f = open('data/day04.txt', 'r')
    grid = [l.strip() for l in  f.readlines()]
    
    total = 0

    while True:
        grid2 = []
        available = 0
        for y in range(0, len(grid)):
            newline = ''
            for x in range(0, len(grid[y])):
                count = 0
                if grid[y][x] != '@':
                    newline += '.'
                    continue
                count = 0
                for i in range( -1 if y > 0 else 0, 2 if y < len(grid) -1 else 1):
                    for j in range( -1 if x > 0 else 0, 2 if x < len(grid[y]) - 1 else 1):
                        if grid[y+i][x+j] == '@':
                            count += 1
                if count <= 4: #neighbours "less than 4" + counting self
                    available += 1
                    newline += '.'
                else:
                    newline += '@'
            grid2.append(newline)
        total += available
        grid = grid2
        if available == 0:
            break
    print(total)

main()