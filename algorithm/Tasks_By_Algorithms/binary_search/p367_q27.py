def binary_first(data,target,n):
  start,last=0,n-1

  while start<=last:
    mid=(start+last)//2
    if (mid==0 or data[mid-1]<target) and data[mid]==target:
      return mid
    elif data[mid]<target:
      start=mid+1
    else:
      last=mid-1

  return -1

def binary_last(data,target,n):
  start,last=0,n-1

  while start<=last:
    mid=(start+last)//2
    if (mid==n-1 or data[mid+1]>target) and data[mid]==target:
      return mid
    elif data[mid]<=target:
      start=mid+1
    else:
      last=mid-1

  return -1
  
n,target=0,0
data_list=[]

with open("input27.txt","r") as file:
  n,target=map(int,file.readline().split())
  data=list(map(int,file.readline().split()))

start_index=binary_first(data,target,n)
if start_index==-1:
  print(-1)
else:
  last_index=binary_last(data,target,n)

  print(start_index,last_index)
  print(last_index-start_index+1)

