import re

def main():
    lines = open('data/day12.txt', 'r').readlines()
    regex = re.compile(r"(\d{2})x(\d{2}): ((?:\d{2}\s?){6})")
    
    fit = 0
    nofit = 0

    cases = 0
    for line in lines:
        match = regex.match(line)
        if match == None:
            continue
        cases += 1
        l = int(match[1])
        w = int(match[2])
        pieces = [int(x) for x in match[3].split(' ')]

        if int(l/3) * int(w/3) >= sum(pieces):
            fit += 1
            continue

        if l * w < 6*pieces[0] + 7*pieces[1] + 5*pieces[2] + 7*pieces[3] + 7*pieces[4] + 7*pieces[5]:
            nofit += 1
            continue

    if fit + nofit == cases:
        print("done!")
    print(fit, nofit)
main()
