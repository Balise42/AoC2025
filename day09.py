def main():
    points = [(int(a[0]), int(a[1])) for a in [line.strip().split(',') for line in open('data/day09.txt', 'r').readlines()]]

    maxArea = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            candidate = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
            if candidate > maxArea:
                maxArea = candidate
    print(maxArea)

    cols = sorted(list(set([point[0] for point in points])))
    rows = sorted(list(set([point[1] for point in points])))

    # assertion checked: no two rows/no two columns are only off by one (which would make adjacency trickier)
    maxArea = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            a = points[i]
            b = points[j]
            (x1,x2) = (points[i][0],points[j][0]) if points[i][0] < points[j][0] else (points[j][0], points[i][0])
            (y1,y2) = (points[i][1],points[j][1]) if points[i][1] < points[j][1] else (points[j][1], points[i][1])
            candidate = (x2-x1+1) * (y2-y1 + 1)
            if candidate > maxArea and isValid(x1, x2, y1, y2, cols, rows, points):
#                print (a,b,candidate)
                maxArea = candidate
    print(maxArea)

# 4715172570 too high

def isValid(x1, x2, y1, y2, cols, rows, points):
    for x in cols:
        if x < x1:
            continue
        if x > x2:
            break
        for y in rows:
            if y < y1:
                continue
            if y > y2:
                break
            if (x,y) in points and ((x != x1 and x!= x2) or (y!=y1 and y!=y2)):
                return False
    return True
main()
