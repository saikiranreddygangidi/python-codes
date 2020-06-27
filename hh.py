arr={}
li = ["xww", "wxyz", "wxyw","ywx","ywz"]
#sorted list
j=1
n1=0
n2=0
for i in range(len(li)-1):
 if li[i]!=li[i+1]:
  if len(li[i])==len(li[i+1]):
   for k in range(len(li[i])):
    if (li[i][k])!=(li[i+1][k]):
     for g in arr:
      if arr[g]==li[i][k]:
       n1=g
      if arr[g]==li[i+1][k]:
       n2=g
     print(n1,n2)
     if n1!=0 and n2!=0:
      if n1>n2:
       arr[n1]=li[i+1][k]
       arr[n2]=li[i][k]
       break
     if n2!=0 and n1==0:
      arr[n2]=li[i+1][k]
      arr[j]=li[i][k]
      j=j+1
      break
     if n1!=0 and n2==0:
      arr[j]=li[i+1][k]
      j=j+1
      break
     if n1==0 and n2==0:
      arr[j]=li[i][k]
      j=j+1
      arr[j]=li[i+1][k]
      j=j+1
      break
  elif len(li[i])<len(li[i+1]):
   for k in range(len(li[i])):
    if (li[i][k])!=(li[i+1][k]):
     for g in arr:
      if arr[g]==li[i][k]:
       n1=g
      if arr[g]==li[i+1][k]:
       n2=g
     if n1!=0 and n2!=0:
      if n1>n2:
       arr[n1]=li[i+1][k]
       arr[n2]=li[i][k]
       break
     if n2!=0 and n1==0:
      arr[n2]=li[i+1][k]
      arr[j]=li[i][k]
      j=j+1
      break
     if n1!=0 and n2==0:
      arr[j]=li[i+1][k]
      j=j+1
      break
     if n1==0 and n2==0:
      arr[j]=li[i][k]
      j=j+1
      arr[j]=li[i+1][k]
      j=j+1
      break
  else:
   for k in range(len(li[i+1])):
    if (li[i][k])!=(li[i+1][k]):
     for g in arr:
      if arr[g]==li[i][k]:
       n1=g
      if arr[g]==li[i+1][k]:
       n2=g
     if n1!=0 and n2!=0:
      if n1>n2:
       arr[n1]=li[i+1][k]
       arr[n2]=li[i][k]
       break
     if n2!=0 and n1==0:
      arr[n2]=li[i+1][k]
      arr[j]=li[i][k]
      j=j+1
      break
     if n1!=0 and n2==0:
      arr[j]=li[i+1][k]
      j=j+1
      break
     if n1==0 and n2==0:
      arr[j]=li[i][k]
      j=j+1
      arr[j]=li[i+1][k]
      j=j+1
      break
h=0
print(arr)
#for h in arr:
# print(arr[h])

 
