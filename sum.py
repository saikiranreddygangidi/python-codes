num=[10,7,76,415]
key={}
arr=[]
a=""
b=""
last=""
k=0
def sum1(digit,value):
 a=""
 b=""
 count=0
 for d in key:
  if d==digit:
   f=d
   count=1
   a=a+str(key[d])
   a=a+str(value)
   b=b+str(value)
   b=b+str(key[d])
   if int(a)>int(b):
    key[d]=a
    break
   else:
    key[d]=b
    break 
 if count==0:
  key[digit]=value
  f=digit
 print(key[f])
 return key[f]
j=0 
for i in range(len(num)):
 n=num[i]
 h=n
 while n>0:
  print(n)
  k=int(n%10)
  n=int(n/10)
 arr.append(k);
 sum1(arr[i],num[i])

print(arr)
i=9
for i in range(9,0,-1):
 for ke in key:
  if ke==i:
   last=last+str(key[ke])
print(last)
