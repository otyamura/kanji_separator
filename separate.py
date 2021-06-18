import re

f = open('kanji.txt', 'r')
data = f.readlines()
f.close()


separate = list()

for i in range(0, len(data)):
    isNum = int()
    isNum = re.sub(r"\D", "", data[i])
    if isNum == '':
        continue
    isNum = int(isNum)
    if (isNum >= 2):
        separate.append(data[i])
        separate.append(data[i+1])

f = open('separated.txt', 'w')
f.writelines(separate)
f.close()