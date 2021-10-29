n=0
input_data=[]

with open("input24.txt","r") as file:
  n=int(file.readline())
  input_data=list(map(int,file.readline().split()))

input_data.sort()
print(input_data[(n-1)//2])