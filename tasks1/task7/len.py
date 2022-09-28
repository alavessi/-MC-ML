f = open('task7.py', 'r')
print(len(''.join(''.join(f.readlines()).split())))
f.close()
