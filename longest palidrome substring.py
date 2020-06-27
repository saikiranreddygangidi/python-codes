b=input()
a=b.lower()
h=0
for i in range(len(a),0,-1):
  k=0
  while(i<=len(a)):
      #print(a[i-1:k:-1]+a[k])
      if(a[k:i]==a[i-1:k:-1]+a[k]):
       h=1;
       print(b[k:i])
       break;
      i+=1
      k+=1
  if(h==1):
   break
#print(a[2:3]+a[3])'''

