import random
num = random.randint(1,50)
trial =0
while(True):
  val = int(input("GUESS THE RANDOM VALUE GENERATED\n"))
  if(num == val):
    trial+=1
    print(trial)
    print("correct guess")
    break
  elif(val>num):
    trial+=1
    print("try little lower")
  elif(val<num):
    trial+=1
    print("try little higher")
  else:
    trial+=1
    print("not the value")
