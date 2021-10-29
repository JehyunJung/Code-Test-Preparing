n=0
input_data=[]

with open("input32.txt","r") as file:
  n=int(file.readline())
  for _ in range(n):
    input_data.append(list(map(int,file.readline().split())))

for i in range(1,n):
  for j in range(i+1):
    target_data=input_data[i][j]
    previous_list=input_data[i-1]

    if j==0:
      input_data[i][j]=previous_list[0]+target_data
    elif j==i:
      input_data[i][j]=previous_list[-1]+target_data
    else:
      input_data[i][j]=max(previous_list[j-1],previous_list[j])+target_data

print(max(input_data[n-1]))