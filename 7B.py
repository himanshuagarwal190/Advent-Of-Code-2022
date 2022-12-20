import collections

file = open("input.txt","r")
ans = 0
dirs = collections.defaultdict(int)
key = '/home'
for line in file:
    line = line.strip()
    if line[:4] == "$ cd":
        if line[-2:] == "..":
            key = key[:key.rfind('/')]
        else:
            key += '/' + line.split(' ')[-1]
    else:
        splits = line.split(' ')
        try:
            size = int(splits[0])
            path = key
            for n in range(path.count('/')):
                dirs[path] += size
                path = path[:path.rfind('/')]
        except:
            pass

toDelete = []
free = 30000000 - (70000000 - dirs['/home'])
for x in dirs:
    if dirs[x] >= free:
        toDelete.append(dirs[x])
toDelete.sort()
print(toDelete[0])
        