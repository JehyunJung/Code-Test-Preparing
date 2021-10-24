num=0
data=[]

with open("input23.txt","r") as file:
  num=int(file.readline())

  for _ in range(num):
    input_data=list(file.readline().split())
    data.append((input_data[0],int(input_data[1]),int(input_data[2]),int(input_data[3])))
sorted_data=sorted(data,key=lambda x:(-x[1],x[2],-x[3],x[0]))

for data in sorted_data:
  print(data[0])