l = list(range(138))
ls = []
for i in l:
        ls.append('"{}"'.format(i))
print(len(ls))
s = ','.join(ls)
print(s)


