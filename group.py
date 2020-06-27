
from itertools import combinations 
n=int(input());a1=[]; count=0;
a=list(map(int,input().split()))
for i in  list(combinations (a, 3)):
 if len(set(i))==3:
     b=sorted(list(i))
     if(b[2]%b[1]==0 and b[1]%b[0]==0):
         if b[2] in a and b[1] in a and b[0] in a:
                 a[a.index(b[0])]=a[a.index(b[2])]=a[a.index(b[1])]=0
                 a1.append(b)
if(len(a1)==n/3):
 print(a1)
else:
 print(-1)