n=int(input())
a=0
b=0
i=0
while True:
 i=i+1
 b=b+1
 if(a+i>n):
  a=a-i
 elif(a+i==n):
  print(b)
  break
 else:
  a=a+i
print('completed')   
  
    
