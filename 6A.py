file = open("input.txt","r")
hashMap = {}
string = ""
for line in file:
    string = line
i = 0
while i < 4:
    hashMap[string[i]] = 1 + hashMap.get(string[i], 0)
    i += 1

if(len(hashMap) == 4):
    print(i+1)
else:
    while i < len(string):
        hashMap[string[i-4]] -= 1
        if hashMap[string[i-4]] == 0:
            del hashMap[string[i-4]]
        hashMap[string[i]] = 1 + hashMap.get(string[i], 0)
        if len(hashMap) == 4:
            print(i+1)
            break
        i += 1

    