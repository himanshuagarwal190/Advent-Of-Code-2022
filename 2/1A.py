file = open('input.txt','r')
strategy = {
    'X': {'C':6, 'A': 3, 'B': 0},
    'Y': {'A': 6, 'B': 3, 'C': 0},
    'Z': {'B': 6, 'C': 3, 'A': 0}
}
extra = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
ans = 0
for x in file:
    opp, you = x[:-1].split(" ")
    num = strategy[you][opp]
    ans += num + extra[you]
print(ans)