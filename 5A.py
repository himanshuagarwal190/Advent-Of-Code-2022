file = open("input.txt","r")
crates = {
    '1': ['D','T','W','F','J','S','H','N'],
    '2': ['H','R','P','Q','T','N','B','G'],
    '3': ['L','Q','V'],
    '4': ['N','B','S','W','R','Q'],
    '5': ['N','D','T','F','V','M','B'],
    '6': ['M','D','B','V','H','T','R'],
    '7': ['D','B','Q','J'],
    '8': ['D','N','J','V','R','Z','H','Q'],
    '9': ['B','N','H','M','S']
}
for line in file:
    _, times, __, frm, ___, to = line.split(' ')
    times = int(times)
    while times > 0:
        ele = crates[frm].pop()
        crates[to[:-1]].append(ele)
        times -= 1
top = ""
for key in crates:
    top += crates[key][-1]
print(top)