#a=[int(x) for x in input().split()]
#even=[]
#odd=[]
a1,b1=0,0
for y in  input().split():
 x=int(y)
 if x&1==0:
     even.append(x)
     a1=a1^x
 else:
     odd.append(x)
     b1=b1^x
if a1!=0 and b1!=0:
    print(a1,'',b1)
elif a1==0:
    key=b1
    odd=sorted(odd)
    for i in range(len(odd)):
        b1^=odd[i]
        if (i+1)&1==0 and b1!=key:
            a1=key^odd[i-1]
            b1=key^a1
            break
    print(a1,'',b1)

elif b1==0:
    key=a1
    even=sorted(even)
    for i in range(len(even)):
        b1^=even[i]
        if (i+1)&1==0 and b1!=key:
            a1=key^even[i-1]
            b1=key^a1
            break
    print(a1,'',b1)
