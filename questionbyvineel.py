def gcd(a,b):
 if(a==b):
  return a;
 elif(a>b):
  return gcd(a-b,b)
 else:
  return gcd(a,b-a)

def gcd1(a):
 k=a[0]
 for i in range(1,len(a)):
  k=gcd(k,a[i])
 return k

a=[int(input()) for i in range(int(input('enter no of values:')))]
b=sorted(a);
max1=gcd1(b[:len(b)-1])+b[-1]
for i in range(-2,-(len(b)+1),-1):
 t=b[-1];b[-1]=b[i];b[i]=t;
 if(max1<(gcd1(b[:len(b)-1])+b[-1])):
  max1=gcd1(b[:len(b)-1])+b[-1];
 t=b[-1];b[-1]=b[i];b[i]=t;
print(max1)
