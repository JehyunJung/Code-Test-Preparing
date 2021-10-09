n=int(input())
data=[]

for i in range(n):
  input_data=input().split()
  data.append((input_data[0],int(input_data[1])))

data.sort(key=lambda x: x[1])

for i in range(n):
  print(data[i][0],end=" ")
print()

