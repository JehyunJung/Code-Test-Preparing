def binary_search(data,target_data,start,end):
  if start > end:
    return None
  
  mid=(start+end)//2

  if data[mid]==target_data:
    return mid
  
  elif data[mid] > target_data:
    return binary_search(data,target_data,start,mid)
  
  else:
    return binary_search(data,target_data,mid+1,end)

n=0
data=[]
with open("data.txt","r") as file:
  n=int(file.readline())
  data=list(map(int,file.readline().split()))
data.sort()

index=binary_search(data,3,0,len(data)-1)
if index:
  print("Index: "+str(index))
else:
  print("Element does not exists")