def main():
    file = open('data/day02.txt', 'r')
    intervalsTxt = file.readline().strip().split(',')

    s = 0
    for interval in intervalsTxt:
        ids = set()
        for base in range(2, 10):
            nums = interval.split('-')
            # length of numbers differs by a single digit at most
            if len(nums[0]) % base != 0 and len(nums[1]) % base != 0:
                continue
            if len(nums[0]) % base == base-1:
                a = 10**len(nums[0])
            else:
                a = int(nums[0])
            if len(nums[1]) % base == base-1:
                b = 10**(len(nums[1])-1)
            else:
                b = int(nums[1])

            strA = str(a)
            strB = str(b)
        
            halfA = strA[:int(len(strA)/base)]

            cand = int(halfA * base)
            while cand <= b:
                if cand >= a:
                    ids.add(cand)
                halfA = str(int(halfA) + 1)
                cand = int(halfA * base)

        for i in range(1, 10):
            for j in range(len(strA), len(strB)+1):
                cand = int(str(i) * j)
                if (cand >= a and cand <= b):
                    ids.add(cand)

        s += sum(ids)

    print(s)

main()
