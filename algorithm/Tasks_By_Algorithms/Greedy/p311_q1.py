n=0
data=[]
result=0
with open("input1.txt","r") as file:
  n=int(file.readline())
  data=list(map(int,file.readline().split()))

data.sort()
count=0

for i in range(n):
  count+=1
  if count>=data[i]:
    result+=1
    count=0

print(result)


