file = open("input.txt","r")
sm = 0
for line in file:
    range1, range2 = line.split(',')
    a,b = range1.split('-')
    x,y = range2.split('-')
    if int(a) >= int(x) and int(b) <= int(y):
        sm += 1
    elif int(x) >= int(a) and int(y) <= int(b):
        sm += 1

print(sm)