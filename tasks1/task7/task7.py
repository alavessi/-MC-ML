import re

def find_shortest(l):
    l = [len(s) for s in re.split(r'[^a-z]', l) if s]
    x = 0
    if l:
        x = min(l)
    return x