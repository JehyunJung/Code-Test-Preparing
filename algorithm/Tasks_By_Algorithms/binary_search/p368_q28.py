def binary_search(data):
  start,end=0,len(data)-1
  
  while start<=end:
    mid=(start+end)//2
    if mid==data[mid]:
      return mid
    elif mid < data[mid]:
      end=mid-1
    else:
      start=mid+1
  return -1
  
test_cases=0
n=0
input_data=[]

with open("input28.txt","r") as file:
  test_cases=int(file.readline())
  for _ in range(test_cases):
    n=int(file.readline())
    input_data=list(map(int,file.readline().split()))
    print(binary_search(input_data))




