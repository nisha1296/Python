hour=raw_input("Enter the number of hours: ")
try:
  h=int(hour)
  rate=raw_input("Enter the rate: ")
  r=int(rate)
  print (float)(h*r)
except:
  print "Please enter a number"  
