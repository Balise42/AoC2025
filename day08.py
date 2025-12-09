def main():
    lines = open('data/day08.txt', 'r').readlines()

    points = []
    for line in lines:
        points.append(tuple([int(x) for x in line.strip().split(',')]))

    dists = {}
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            (x1, y1, z1) = points[i]
            (x2, y2, z2) = points[j]
            dists[(points[i], points[j])] = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

    sortedPairs = sorted(dists.keys(), key=lambda p: dists[p])
   
    components = {}
    compid = 1
    links = 0
    while True:

        if links == 1000:
            comps = {}
            for k, v in components.items():
                if not v in comps:
                    comps[v] = []
                comps[v].append(k)
            res = sorted([len(v) for v in comps.values()])
            print(res[-1] * res[-2] * res[-3])

        if len(set(components.values())) == 1 and len(components) == len(points):
            print(a[0]*b[0])
            break
            

        links += 1
        (a, b) = sortedPairs.pop(0)
        if not a in components and not b in components:
            components[a] = compid
            components[b] = compid
            compid+=1
        elif a in components and b in components:
            if components[a] == components[b]:
                continue
            else:
                merged = components[b]
                tomerge = components[a]
                for k,v in components.items():
                    if v == tomerge:
                        components[k] = merged
        elif a in components:
            components[b] = components[a]
        elif b in components:
            components[a] = components[b]


main()
