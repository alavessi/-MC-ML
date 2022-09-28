from collections import defaultdict

def check(s: str, file: str):
    d = defaultdict(int)
    for word in sorted(s.lower().split()):
        d[word] += 1
    f = open(file, 'w')
    for word, count in d.items():
        f.write(word + ' ' + str(count) + '\n')
    f.close()
