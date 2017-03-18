count,total,avg=0,0,0.0
while True:
  inp=raw_input("Enter a number: ")
  try:
    if inp=='done':
      break
    total=total+int(inp)
    count=count+1
  except:
    print "Invalid Input"
print "count: ",count,"\nTotal: ",total,"Average: ",(float)((float)(total)/count)      
