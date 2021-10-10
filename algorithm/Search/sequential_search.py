n=0
data=[]

with open("data.txt","r") as file:
  n=int(file.readline())
  data=list(map(int,file.readline().split()))

for i in range(n):
  if data[i]==3:
    print("index: "+str(i+1))
    break