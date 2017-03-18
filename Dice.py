import random
num=(int)(random.randint(0,1000))
print(num)
i=1
while(i):
  guess=raw_input("Enter your guess: ")
  try:
    val=int(guess)
  except ValueError:
    print("Invalid number")  
  if val==num:
    print("Congrats")
    i=0
  elif(val<num):
    print("Value too less")
  else:
    print("Value too high")    
      
