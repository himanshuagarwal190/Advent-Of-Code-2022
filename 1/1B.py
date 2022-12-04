file = open("input.txt","r")
sum1 = 0
sum2 = 0
sum3 = 0
sm = 0
for num in file:
    if num == "\n":
        if sm >= sum1:
            sum3 = sum2
            sum2 = sum1
            sum1 = sm
        elif sm >= sum2:
            sum3 = sum2
            sum2 = sm
        elif sm >= sum3:
            sum3 = sm
        sm = 0
    else:
        sm += int(num)
print(sum1+sum2+sum3)