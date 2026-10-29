f = open('命运.txt', 'r')
txt = f.read()
d = {}
for i in txt:
    if i not in "，。？！《》【】“”‘’":
        d[i] = d.get(i, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
print("{}:{}".format(ls[0][0], ls[0][1]))
f.close()
