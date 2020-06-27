s=15
n=7 #if we want we can dynamically also value of s,n,m
m=5
count=0
count1=0
count2=0
left=0
if n<m:
 print("no")
else:
 k=s*m
 if k<=n:
  print("1")
 else:
  while k>n:
   k=k-n
   left=left+(n-m)
   count=count+1
   if (count)%7==0:
    if left>=m:
     count=count+1
     count1=count1+1
    else:
     count2=1
     print("no")
     break
   if k<=n:
    count=count+1
    break
if (count-count1)<=s and count2==0:
 print(str(count-count1))
elif count2==0:
 print("no")
  
