d = { 'b':1, 'c': 22,'a': 10}
dict_items = ([('b',1), ('c', 22),('a', 10), ])
for k,v in sorted(d.items(), reverse=True):
    print(k, v)
print(sorted(d.items(), reverse=True))