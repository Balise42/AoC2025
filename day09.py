def main():
    points = [(int(a[0]), int(a[1])) for a in [line.strip().split(',') for line in open('data/day09.txt', 'r').readlines()]]

    maxArea = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            candidate = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
            if candidate > maxArea:
                maxArea = candidate
    print(maxArea)

    maxArea = 0
    prev = points[0]
    horizontals = []
    verticals = []
    for i in range(1, len(points)):
        if prev[1] == points[i][1]:
            horizontals.append((prev, points[i]) if prev[0] < points[i][0] else (points[i], prev))
        else:
            verticals.append((prev, points[i]) if prev[1] < points[i][1] else (points[i], prev))
        prev = points[i]
    if prev[0] == points[0][0]:
            verticals.append((prev, points[0]) if prev[1] < points[0][1] else (points[0], prev))
    else:
       horizontals.append((prev, points[0]) if prev[0] < points[0][0] else (points[0], prev))

    horizontals.sort(key=lambda p: p[0][1])
    verticals.sort(key=lambda p: p[0][0])

    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            a = points[i]
            b = points[j]
            (x1, x2) = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
            (y1, y2) = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])
            candidate = (x2-x1+1) * (y2-y1 + 1)
            if candidate > maxArea and isValid(x1, x2, y1, y2, horizontals, verticals):
                maxArea = candidate
    print(maxArea)

def isValid(x1, x2, y1, y2, horizontals, verticals):
    for p in horizontals:
        if p[0][1] <= y1:
            continue
        if p[0][1] >= y2:
            break
        a = p[1][0] <= x1
        b = p[0][0] >= x2
        if (not(a or b)):
            return False
    for p in verticals:
        if p[0][0] <= x1:
            continue
        if p[0][0] >= x2:
            break
        a = p[1][1] <= y1
        b = p[0][1] >= y2
        if (not (a or b)):
            return False

    return True
main()
