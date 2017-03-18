x=int(raw_input("Enter the first number: "))
y=int(raw_input("Enter the second number: "))
if x<=y:
  if x==y:
    print("%d is equal to %d\n" %(x,y))
  else:
    print("%d is less than %d\n" %(x,y))
else:
  print("%d is greater than %d\n" %(x,y))      
