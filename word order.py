from collections import OrderedDict

words = OrderedDict()

for i in range(int(input())):
    key = input()
    if key in words:
        words[key] += 1
    else:
        words[key] = 1

string= ' '.join(map(str, words.values()))
print(string)