
count,total=0,0
list1=[]
while True:
  inp=raw_input("Enter a number: ")
  try:
    if inp=='done':
      break
    total=total+int(inp)
    list1.append(inp)
    count=count+1
  except:
    print "Invalid Input"
print "count: ",count,"\nTotal: ",total,"Max: ",max(list1),"Min: ",min(list1)
