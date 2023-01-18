file = open("input.txt","r")
rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
visited = set()
visited.add(tuple(rope[0]))
for line in file:
    direction, count = line.strip().split(' ')
    count = int(count)
    print(rope)
    print('------')
    if direction == "U":
        while count > 0:
            rope[-1][1] += 1
            count -= 1
            i = 9
            while i > 0:
                if rope[i][1] - rope[i-1][1] > 1:
                    if (abs(rope[i-1][0] - rope[i][0]) > 1):
                        rope[i-1][0] = rope[i][0]
                    rope[i-1][1] += 1
                i -= 1
            print(rope[0])
            visited.add(tuple(rope[0]))
    elif direction == "D":
        while count > 0:
            rope[-1][1] -= 1
            count -= 1
            i = 9
            while i > 0:
                if rope[i][1] - rope[i-1][1] > 1:
                    rope[i-1][0] = rope[i][0]
                    rope[i-1][1] -= 1
                i -= 1
            print(rope[0])
            visited.add(tuple(rope[0]))
    elif direction == "R":
        while count > 0:
            rope[-1][0] += 1
            count -= 1
            i = 9
            while i > 0:
                if rope[i][0] - rope[i-1][0] > 1:
                    rope[i-1][1] = rope[i][1]
                    rope[i-1][0] += 1
                i -= 1
            print(rope[0])
            visited.add(tuple(rope[0]))
    elif direction == "L":
        while count > 0:
            rope[-1][0] -= 1
            count -= 1
            i = 9
            while i > 0:
                if abs(rope[i][0] - rope[i-1][0]) > 1:
                    rope[i-1][1] = rope[i][1]
                    rope[i-1][0] -= 1
                i -= 1
            print(rope[0])
            visited.add(tuple(rope[0]))
            
print(len(visited))