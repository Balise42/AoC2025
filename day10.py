import re
import numpy as np
import math

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
        A = np.array([[0.0 for x in toggleList] for y in voltageList])
        for i in range(len(toggleList)):
            for t in toggleList[i]:
                A[t][i] = 1

        voltageList = np.transpose(np.array([voltageList]))

        # happy case: we have n equations, n unknown, solve is done
        cansolve = True
        try:
            x = np.linalg.solve(A, voltageList)
        except:
            cansolve = False

        if cansolve:
            res2 += round(sum(x)[0])
            continue
        
        clicks = sum(voltageList)[0] + 20
        voltMax = round(max(voltageList)[0]+1)

        (G, V) = gauss(A, voltageList)
        # 31101 too high
        # nope on 29545
        # nope on 20692
        # nope on 20696
        # nope on 20687
        # nope on 20694
        # nope on 20695
        # nope on 20880

        indices = []
        for i in range(len(G[0])):
            if i - len(indices) < len(G) and G[i-len(indices)][i] == 1:
                continue
            indices.append(i)
       
        free = len(indices)
        if free > 3:
            raise Exception('aaaa')
            
        sus = True
        for i3 in range(voltMax+1 if free > 2 else 1):
            for i2 in range(voltMax+1 if free > 1 else 1):
                for i in range(voltMax+1 if free > 0 else 1):
                    if i + i2 + i3 > voltMax:
                        continue
                    D = V.copy()
                    if free > 0:
                        D = D - i*np.transpose([np.array(G[..., indices[0]])])
                    if free > 1:
                        D = D - i2*np.transpose([np.array(G[..., indices[1]])])
                    if free > 2:
                        D = D - i3*np.transpose([np.array(G[..., indices[2]])])
                    valid = True
                    cand = 0
                    D = D.flatten()
                    for d in range(len(D)):
                        if D[d] < -0.000000001:
                            valid = False
                            break
                        if abs(round(D[d]) - D[d]) > 0.000000001:
                            valid = False
                            break
                        D[d] = round(D[d])
                        nonZero = False
                        for k in range(len(G[d])):
                            if k not in indices:
                                if G[d][k] != 0 and G[d][k] != 1:
                                    print('sus')
                                    print(G)
                                    exit()
                                if round(G[d][k]) != 0:
                                    nonZero = True
                        if nonZero:
                            cand += D[d]
                    cand += i + i2 + i3
                    if valid and cand < clicks:
                        sus = False
                        S = []
                        t = 0
                        ts = 0
                        while True:
                            if t >= len(A[0]):
                                break
                            if t in indices:
                                if t == indices[0]:
                                    S.append(i)
                                elif t == indices[1]:
                                    S.append(i2)
                                else:
                                    S.append(i3)
                            else:
                                S.append(round(D[ts]))
                                ts += 1
                            t += 1
                        S = np.transpose(np.array([S]))
                        if not np.all(np.matmul(A, S) == voltageList):
                            print('not a solution')
                            print(line)
                            print(A)
                            print(S)
                            print(G)
                            print(V)
                            print(D)
                            print(voltageList)
                            print(indices, i, i2, i3)
                            exit()
                        clicks = round(cand)
        if sus:
            print('sus')
            print(G)
            print(V)
            exit()
        res2+=clicks

    print(res)
    print(res2)

def gauss(A, B):
    aug = np.hstack((A, B))
    
    h = 0
    k = 0
    while h < len(aug) and k < len(aug[0]):
        col = np.ndarray.flatten(aug[:, k])
        imax = -1
        valp = 0
        for i in range(h, len(col)):
            if abs(col[i]) > valp:
                valp = abs(col[i])
                imax = i
        if valp == 0:
            k += 1
            continue
        aug[[imax, h]] = aug[[h, imax]]
        aug[h] = aug[h] / aug[h][k]
        for i in range(len(aug)):
            if (i != h):
                aug[i] = aug[i] - aug[h] * aug[i][k]
        for i in range(len(aug)):
            for j in range(len(aug[i])):
                if abs(round(aug[i][j]) - aug[i][j]) < 0.0000001:
                    aug[i][j] = round(aug[i][j])
        h += 1
        k += 1
    newV = aug[:, -1:]
    C = np.delete(aug, len(aug[0]) - 1, axis = 1)
    return (C, newV)


def hamming(X, Y):
    dist = 0
    for i in range(len(X)):
        if X[i] != Y[i]:
            dist += 1
    return dist

def makeNeigh(node, toggle):
    neigh = ''
    for i in range(0, len(node)):
        if i in toggle:
            neigh += '.' if node[i] == '#' else '#'
        else:
            neigh += node[i]
    return neigh

main()
