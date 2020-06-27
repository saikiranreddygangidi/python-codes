a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[]
min=cols=rows=i=0;max=3;
while(max>=min ):
   if(i%2==0):
    b.extend(a[min][min:max+1])
    for h in range(min+1,max+1):
     b.append(a[h][max])
    i=i+1
   else:
    min=min+1
    max=max-1
    b.extend(a[max+1][max:min-1:-1])
    for h in range(max+1,min-1,-1):
     b.append(a[h][min-1])
    i=i+1
print(b)
