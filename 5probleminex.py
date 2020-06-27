n=int(input())
a=[list(input().split()) for x in range(n)]
c=[1 for x in range(n)]
b=[list(c) for x in range(n)]
mi,ma=0,n-1
i=j=mi
while(mi<ma):
 i=j=mi
 if(i==mi):
  while(j!=ma):
   b[i][j+1]=a[i][j]
   print(a[i][j])
   j=j+1
  else:
   while(i!=ma):
    b[i+1][j]=a[i][j]
    i+=1
   else:
    while(j!=mi):
     b[i][j-1]=a[i][j]
     j-=1
    else:
     while(i!=mi):
      b[i-1][j]=a[i][j]
      i-=1
     else:
      mi+=1
      ma-=1

print(b)
            
                
