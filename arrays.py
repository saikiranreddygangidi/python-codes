 a=[[1,2,3],[4,5,6],[7,8,9]]
 b=[]
 min=cols=rows=i=0;max=2;
 while(max>=min ):
   if(i%2==0):
    b.append(a[min,min:max+1]+a[min:max+1,max])
	i=i+2
   else:
    b.append(a[max][max:min-1:-1])
     min=min+1
	 max=max-1
	b.append(a[max:min-1:-1][min-1]) 