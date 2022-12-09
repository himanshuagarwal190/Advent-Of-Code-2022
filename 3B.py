import collections
file = open("input.txt","r")
sum = 0
count = 1
common = collections.defaultdict(int)
for line in file:
    st = set(line)
    for x in st:
        common[x] += 1
    if count == 3:
        for x in common:
            if common[x] == 3 and x != "\n":
                if ord(x) - ord('a') >= 0:
                    sum += ord(x) - ord('a') + 1
                else:
                    sum += 26 + ord(x) - ord('A') + 1
        count = 0
        common = collections.defaultdict(int)
    count += 1
    
print(sum)