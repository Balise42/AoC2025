import re

def main():
    lines = open('data/day10-sample.txt', 'r').readlines()

    regex = re.compile(r"""\[([.#]*)]+ ([\d,\(\)\s]+) {([\d,]+)}""")
    res = 0
    res2 = 0
    for line in lines:
        strState = regex.match(line)[1]
        strToggles = regex.match(line)[2]
        strVoltages = regex.match(line)[3]

        toggleList = [[int(d) for d in c] for c in [b.split(',') for b in [a[1:-1] for a in strToggles.split(' ')]]]
        node = '.'*len(strState)
        visited = {}
        visited[node] = 0
        queue = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            for toggle in toggleList:
                neigh = makeNeigh(node, toggle)
                if neigh in visited:
                    continue
                visited[neigh] = visited[node] + 1
                queue.append(neigh)
                if neigh == strState:
                    queue = []
                    res += visited[neigh]
                    break
        
        voltageList = [int(a) for a in strVoltages.split(',')]
        end = ','.join(['0' for i in range(0, len(voltageList))])
        visited = {}
        visited[strVoltages] = 0
        start = strVoltages
        queue = [strVoltages]
        while len(queue) > 0:
            nodeStr = queue.pop(0)
            node = [int(a) for a in nodeStr.split(',')]
            minNode = max(node)
            for i in node:
                if i < minNode and i > 0:
                    minNode = i
            minIndex = node.index(minNode)
            for toggle in toggleList:
                if minIndex not in toggle:
                    continue
                neigh = makeNeigh2(nodeStr, toggle, minNode) 
                if neigh in visited and visited[neigh] <= minNode + visited[nodeStr]:
                    continue
                visited[neigh] = visited[nodeStr] + minNode
                queue.append(neigh)
                if neigh == end:
                    queue = []
                    print(visited[neigh])
                    res2 += visited[neigh]
                    break

    print(res)
    print(res2)

def makeNeigh(node, toggle):
    neigh = ''
    for i in range(0, len(node)):
        if i in toggle:
            neigh += '.' if node[i] == '#' else '#'
        else:
            neigh += node[i]
    return neigh

def makeNeigh2(nodeStr, toggle, minNode):
    node = [int(a) for a in nodeStr.split(',')]
    for i in range(0, len(node)):
        if i in toggle:
            node[i] -= minNode
    return ','.join([str(i) for i in node])

def invalid(neigh, voltage):
    neighList = [int(a) for a in neigh.split(',')]
    for i in range(0, len(neighList)):
        if neighList[i] > voltage[i]:
            return True
    return False


main()
