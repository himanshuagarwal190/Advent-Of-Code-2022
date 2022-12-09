file = open("input.txt","r")
sum = 0
for line in file:
    ln = len(line)
    first = set(line[:ln//2])
    common = set()
    for x in line[ln//2:]:
        if x in first:
            common.add(x)
    for x in common:
        if ord(x) - ord('a') >= 0:
            sum += ord(x) - ord('a') + 1
        else:
            sum += 26 + ord(x) - ord('A') + 1
print(sum)