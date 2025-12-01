def main():
    pos = 50
    password = 0
    password2 = 0

    file = open('data/day01.txt', 'r')
    for line in file:    
        dir = line[0]
        clicks = int(line[1:])
        if dir == 'R':
            if (pos != 0 and pos + clicks % 100 > 100):
                password2 += 1
            pos = (pos + (clicks)%100) % 100
        else:
            if (pos != 0 and pos - clicks % 100 < 0):
                password2 += 1
            pos = (pos - (clicks)%100) % 100
        if pos == 0:
            password += 1
            password2 += 1
        password2 = password2 + clicks // 100
        
    print(password2)


#6492 too high
main()