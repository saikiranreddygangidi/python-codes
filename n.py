  a=[]
from functools import partial
for line in iter(partial(input, 'Please enter value: '), ''):
    a.append(line)
print(a)
