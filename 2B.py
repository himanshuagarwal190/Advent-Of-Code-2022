file = open('input.txt','r')
strategy = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'}
}
extra = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
choose = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
ans = 0
for x in file:
    opp, you = x[:-1].split(" ")
    choice = strategy[you][opp]
    ans += choose[you] + extra[choice]
print(ans)