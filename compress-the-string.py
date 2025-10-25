from itertools import groupby

s = input()

s_groups = []
for k,g in groupby(s):
    s_groups.append(tuple([len(list(g)),int(k)]))

encoded_s = ''
for t in s_groups:
    encoded_s += str(t) + ' '

print(encoded_s.rstrip())