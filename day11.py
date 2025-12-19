def main():
    lines = open('data/day11.txt').readlines()

    graph = {}
    for line in lines:
        toks = line.strip().split(' ')
        
        inp = toks[0][0:-1]
        out = toks[1:]
        
        for o in out:
            if o not in graph:
                graph[o] = []
            graph[o].append(inp)
   
    
    memo = {'you': 1}
    print(numpaths('out', memo, graph))

    memo = {'fft': 1}
    midpaths = numpaths('dac', memo, graph)
    memo = {'svr': 1}
    startpath = numpaths('fft', memo, graph)
    memo = {'dac': 1}
    endpath = numpaths('out', memo, graph)

    print(startpath * midpaths * endpath)

def numpaths(out, memo, graph):
    if out in memo:
        return memo[out]
    paths = sum([numpaths(i, memo, graph) for i in (graph[out] if out in graph else [])])
    memo[out] = paths
    return paths


main()
