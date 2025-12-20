import re
import copy
import random

class Light:
    target = 0
    toggles = []
    
    def __init__(self, target, toggles):
        self.target = target
        self.toggles = toggles

    def click(self,toggle, times):
        if toggle in self.toggles:
            self.target -= times
            self.toggles.remove(toggle)
    
    def isValid(self):
        if len(self.toggles) == 0:
            return self.target == 0
        return self.target >= 0

    def __str__(self):
        return "{} {}".format(self.target, self.toggles)
    

class State:
    lights = []
    clicks = {}

    def __init__(self, lights):
        self.lights = lights

    def __str__(self):
        res = ""
        for i in self.lights:
            res += "{}   ".format(i)
        res += " {}".format(self.clicks)
        return res
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(other):
        return str(other) == str(self)

    def click(self):
        self.lights.sort(key=lambda l: len(l.toggles)*1000 + l.target)
        light = self.lights[0]
        if light.target == 0:
            self.lights.pop(0)
            return [self]
        if len(light.toggles) == 1:
            self.lights.pop(0)
            nl = []
            for l in self.lights:
                nl.append(Light(l.target, l.toggles.copy()))
            ns = State(nl)
            ns.clicks = self.clicks.copy()
            ns = ns.clickToggle(light.toggles[0], light.target)
            if (ns.isValid()):
                return [ns]
            else:
                return []

        res = []
        tog = light.toggles[0]
        for i in range(0, light.target+1):
            nl = []
            for l in self.lights:
                nl.append(Light(l.target, l.toggles.copy()))
            ns = State(nl)
            ns.clicks = self.clicks.copy()
            att = ns.clickToggle(tog, i)
            if att.isValid():
                res.append(att)
            else:
                break
        return res

    def clickToggle(self, toggle, times):
        for light in self.lights:
            light.click(toggle, times)
        self.clicks[toggle] = times
        return self
 

    def isValid(self):
        for light in self.lights:
            if not light.isValid():
                return False
        return True

    

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

        lights = []

        for i in range(len(voltageList)):
            v = voltageList[i]
            light = Light(v, [])
            for j in range(len(toggleList)):
                toggle = toggleList[j]
                if i in toggle:
                    light.toggles.append(j)

            lights.append(light)
        
        state = State(lights)
        states = [state]
        num = 1000000
        while len(states) > 0:
            s = states.pop(0)
            if len(s.lights) == 0:
                cand = sum(s.clicks.values())
                if (num > cand):
                    num = cand
                continue
            states.extend(s.click())
        res2 += num
        print(num)

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
