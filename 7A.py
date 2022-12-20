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
        if line.startswith('dir'): continue
        splits = line.split(' ')
        try:
            size = int(splits[0])
            path = key
            for n in range(path.count('/')):
                dirs[path] += size
                path = path[:path.rfind('/')]
        except:
            pass
for x in dirs:
    if dirs[x] < 100000:
        ans += dirs[x]
print(ans)
        