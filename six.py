for i in range(1,6):
    a=[]
    for j in range(1,i+1):
        a.append(str(j))
    n=9-2*i
    for k in range(n):
        a.append(' ')
    if(i!=5):
     for j in range(i,0,-1):
         a.append(str(j))
    else:
     for j in range(i-1,0,-1):
         a.append(str(j))
    print(''.join(a))
