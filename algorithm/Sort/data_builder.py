import random
n=1000
with open("big_data.txt","w") as file:
  file.write(str(n)+"\n")
  for _ in range(n):
    file.write(str(random.randint(0,1000))+" ")
