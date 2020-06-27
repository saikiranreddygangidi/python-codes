import collections
str1 = 'jiujitsu'
a=list(str1);
d = collections.defaultdict(int)
for c in str1:
 d[c] += 1
max=0
for c in sorted(d, key=d.get, reverse=True):
 if d[c] > 1 and a.index(c)>max:
  max=a.index(c)
for c in sorted(d, key=d.get, reverse=True):
  
