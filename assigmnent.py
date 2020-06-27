A=[int(input()) for x in range(int(input("enter no of values")))]
x=int(input("enter  value"))
c=0
for s in A:
 if(s==x):
  print(x,"is present in list")
  c=1
if(c==0):
  print(x,"is present not in list")
#we can directly use in keyword for finding
if(x in A):
 print(x,"is present in list")
elif(x not in A):
 print(x,"is present not in list")
print("min in the list is",min(A))
print("max in the list is",max(A))
print("index is",A.index(x))
print("count is",A.count(x))
