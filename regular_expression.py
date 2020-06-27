import re

line = "jiijiutsu"

searchObj = re.search( r'(.*)j(.*)i(.*)u(.*)|(.*)i(.*)j(.*)u(.*)', line[2:], re.M|re.I)

if searchObj:
 print ("searchObj.group() :", searchObj.group())
else:
 print("Nothing found!!")

