inp=raw_input("Enter filename: ")
try:
  fp=open(inp)
except:
  print "No such file exists. "
  exit()
count=0
for i in fp:
  count=count+1
print "Line count: ",count      
