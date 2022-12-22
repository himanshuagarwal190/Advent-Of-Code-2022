file = open("input.txt","r")
ip = []
for line in file:
    arr = [int(x) for x in list(line.strip())]
    ip.append(arr)

R,C = len(ip), len(ip[0])
mx = 0

for r in range(R):
    for c in range(C):
        #bottom
        count = 0
        score = 1
        for i in range(r+1, R):
            count += 1
            if ip[r][c] <= ip[i][c]:
                break
        #top
        score *= count
        count = 0
        for i in range(r-1, -1,-1):
            count += 1
            if ip[r][c] <= ip[i][c]:
                break
        #right
        score *= count
        count = 0
        for i in range(c+1, C):
            count += 1
            if ip[r][c] <= ip[r][i]:
                break
        #left
        score *= count
        count = 0
        for i in range(c-1, -1,-1):
            count += 1
            if ip[r][c] <= ip[r][i]:
                break
        score *= count
        mx = max(mx, score)
print(mx)