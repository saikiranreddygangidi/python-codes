#prime numbers
''''
a=[True]*(n+1)
for i in range(2,n+1):
	if a[i]==True:
	 for j in range(i*2,n+1,i):
	 	a[j]=False
for i in range(1,n+1):
  if(a[i]==True):
  	 print(str(i))'''
#pow function in O(1)

a=int(input())
b=int(input())
ans=1;x=a;
if(b&1):
    print('odd')
else:
    print('even')
for i in range(0,10):
 print(str(i))
 print('hi')
 if(b & 1):
  print('hi-1')
  ans*=x
 b=b>>1
 x*=x
print(ans)
