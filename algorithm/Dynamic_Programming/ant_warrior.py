def search_food(arr,n):
  d=[0]*(n+1)
  d[0]=0
  d[1]=arr[0]

  for i in range(2,n+1):
    d[i]=max(d[i-1],d[i-2]+arr[i-1])
  
  return d[i]

n=0
input_data=[]

with open("input.txt","r") as file:
  n=int(file.readline())
  input_data=list(map(int,file.readline().split()))

print(search_food(input_data,n))


