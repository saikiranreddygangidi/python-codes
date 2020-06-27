a,b,c,count=input(),[],'',0
for i in a:
    if(i!=c):
        b.extend([str(count),i]);c=i;count=1;
    else:
        count+=1
b.append(str(count))
print(''.join(b[1:]))
     
