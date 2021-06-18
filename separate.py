import re

f = open('kanji.txt', 'r')
data = f.readlines()
f.close()


separate = list()

for i in range(0, len(data), 2):
    isNum = int()
    isNum = re.sub(r"\D", "", data[i])
    isNum = int(isNum)
    if (isNum >= 2):
        separate.append(data[i])
        separate.append(data[i+1])

f = open('separated.txt', 'w')
f.writelines(separate)
f.close()

# 正規表現用に漢字のみをパイプでつなげる

kanjis = str()

for i in range(1, len(separate), 2):
    kanjis += separate[i].replace(' ', '|')

kanjis = kanjis.replace('\n', '|')
kanjis = kanjis.rstrip('|')

print(kanjis)