file = open("input.txt","r")
sum = 0
ans = 0
for num in file:
    if num == "\n":
        ans = max(ans, sum)
        sum = 0
    else:
        sum += int(num)
print(ans)