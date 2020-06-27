sum=0
count=0
def throw_dice(n,faces,total):
 if total>(n*faces):
  print("can not do")
 else:
  another(n,sum,total)
  global count
  print(count)
  
def another(n,sum,total):
 if n==1:
  for i in range(1,total+1):
   if (sum+i)==total:
    global count
    count=count+1
 else:
  for i in range(1,total+1):
   another(n-1,sum+i,total)  
throw_dice(int(input()),int(input()),int(input()))
