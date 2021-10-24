import bisect
  
n,target=0,0
data_list=[]

with open("input27.txt","r") as file:
  n,target=map(int,file.readline().split())
  data=list(map(int,file.readline().split()))

start_index=bisect.bisect_left(data,target,0,n-1)
if start_index==-1:
  print(-1)
else:
  last_index=bisect.bisect_right(data,target,0,n-1)

print(last_index-start_index)

