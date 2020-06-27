arr={}
li = ["xww", "wxyz", "wxyz","ywx","ywz"]
#sorted list
j=1
for i in range(len(li)-1):
 if li[i]!=li[i+1]:
  if len(li[i])==len(li[i+1]):
   for k in range(li[i]):
    if (li[i][k])!=(li[i+1][k]):
	 arr[j]=li[i][k]
	 j++
	 arr[j]=li[i+1][k]
	 j++
	 break
  elif len(li[i])<len(li[i+1]):
   for k in range(li[i]):
	if li[i][k]!=li[i+1][k]:
	 arr[j]=li[i][k]
	 j++
	 arr[j]=li[i+1][k]
	 j++
	 break
  else:
   for k in range(li[i+1]):
	if li[i][k]!=li[i+1][k]:
	 arr[j]=li[i][k]
	 j++
	 arr[j]=li[i+1][k]
	 j++
	 break

for h in range(j):
 print(arr[h])
 