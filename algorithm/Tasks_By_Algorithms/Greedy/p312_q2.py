data=0
with open("input2.txt","r") as file:
  data=list(file.readline())

result=0
result=int(data[0])
for i in range(1,len(data)):
  target=int(data[i])

  if target<=1 or result<=1:
    result+=target
  else:
    result*=target

print(result)
