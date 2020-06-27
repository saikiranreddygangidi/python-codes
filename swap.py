#nums = [int(x) for x in user_input.split()[:n]]
n=int(input("enter n value"))
a=[]
b={}
t=0;
d=[]
for i in range(n):
 num=int(input("enter next no"))
 if num<n:
  b[i]=num
  a.append(num)
 else:
  a.append(num)
c=list(input("enter str"))
for d1 in b:
 for d2 in b:
  if d1==b[d2] and d2==b[d1] and (d1 not in d) or (d2 not in d):
   d.append(int(d1))
   d.append(int(d2))
   t=c[d1]
   c[d1]=c[d2]
   c[d2]=t
print(c)
