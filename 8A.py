file = open("input.txt","r")
ip = []
for line in file:
    arr = [int(x) for x in list(line.strip())]
    ip.append(arr)

R,C = len(ip), len(ip[0])
count = 0

for r in range(R):
    for c in range(C):
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            count += 1
            continue
        #bottom
        bottom = True
        for i in range(r+1, R):
            if ip[r][c] <= ip[i][c]:
                bottom = False
                break
        #top
        top = True
        for i in range(r-1, -1,-1):
            if ip[r][c] <= ip[i][c]:
                top = False
                break
        #right
        right = True
        for i in range(c+1, C):
            if ip[r][c] <= ip[r][i]:
                right = False
                break
        #left
        left = True
        for i in range(c-1, -1,-1):
            if ip[r][c] <= ip[r][i]:
                left = False
                break
        if top or bottom or left or right:
            count += 1
print(count)