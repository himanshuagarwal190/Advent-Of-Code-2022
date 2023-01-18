file = open("input.txt","r")
head = [0,0]
tail = [0,0]
visited = set()
for line in file:
    direction, count = line.strip().split(' ')
    count = int(count)
    if direction == "U":
        while count > 0:
            head[1] += 1
            count -= 1
            if head[1] - tail[1] > 1:
                tail[0] = head[0]
                tail[1] += 1
            visited.add(tuple(tail))
    elif direction == "D":
        while count > 0:
            head[1] -= 1
            count -= 1
            if abs(head[1] - tail[1]) > 1:
                tail[0] = head[0]
                tail[1] -= 1
            visited.add(tuple(tail))
    elif direction == "R":
        while count > 0:
            head[0] += 1
            count -= 1
            if head[0] - tail[0] > 1:
                tail[1] = head[1]
                tail[0] += 1
            visited.add(tuple(tail))
    elif direction == "L":
        while count > 0:
            head[0] -= 1
            count -= 1
            if abs(head[0] - tail[0]) > 1:
                tail[1] = head[1]
                tail[0] -= 1
            visited.add(tuple(tail))
print(len(visited))