import operator
s=input()
stats={}
hh=s[:]

for i in s:
 stats[i]=hh.count(i)

for i in range(3):
 d=dict(max(stats.items(), key=operator.itemgetter(1)))
 b=min(d)
 print(b,stats[b])
 stats.pop(b)
