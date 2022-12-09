file = open("input.txt","r")
sm = 0
for line in file:
    range1, range2 = line.split(',')
    a,b = range1.split('-')
    x,y = range2.split('-')
    if int(b) >= int(x) and int(a) <= int(y):
        sm += 1
    elif int(y) >= int(a) and int(x) <= int(b):
        sm += 1

print(sm)