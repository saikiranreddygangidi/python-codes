a=[int(input()) for i in range(int(input("enter noof wall")))]
total=0;f=1111110;
if len(a)!=2 and min(a)!=0 or a != sorted(a) or a!=reversed(sorted(a)):
    for i in range(len(a)):
        if(i+2!=len(a)):
            if(a[i]==a[i+1]==a[i+2]==0):
                total+=f
            if(min(a[i],a[i+2])>a[i+1]):
                total+=(min(a[i],a[i+2])-a[i+1])
                f=(min(a[i],a[i+2])-a[i+1])
                #print("e1-",total)
            else:
                if(i==0 and min(a[i],a[i+2])!=a[i]) or (i+2==(len(a)-1)and min(a[i],a[i+2])!=a[i+2] ):
                 if a[i+1]<=max(a[i],a[i+2]):
                    total+=(max(a[i],a[i+2])-a[i+1])
                     f=(max(a[i],a[i+2])-a[i+1])
                else:
                 if( min(a[i],a[i+2])==a[i] or a[i]==a[i+1]):
                  if a[i+1]<=max(a[i],a[i+2]):
                    total+=(max(a[i],a[i+2])-a[i+1])
                     f=(max(a[i],a[i+2])-a[i+1])
                    
        else:
            break;

print(total);
