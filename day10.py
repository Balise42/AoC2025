import re
import numpy as np

def main():
    lines = open('data/day10.txt', 'r').readlines()

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
        matrix = [[0 for i in range(len(toggleList))] for j in range(len(voltageList))]
        for i in range(len(toggleList)):
            t = toggleList[i]
            for j in range(len(t)):
                matrix[t[j]][i] = 1
        matrix = np.matrix(matrix)
        print(matrix)
        print(voltageList)
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

main()
