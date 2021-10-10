def binary_search(data,target_data,start,end):
  result=0
  while start<=end:
    mid=(start+end)//2
    temp=[x-mid for x in data if x > mid]

    if sum(temp)<target_data:
      end=mid-1
    else:
      result=mid
      start=mid+1
      
  return result

if __name__ == "__main__":
  n,m=0,0
  data=[]
  with open("input.txt","r") as file:
    n,m=map(int,file.readline().split())
    data=list(map(int,file.readline().split()))

  result=binary_search(data,m,0,max(data))
  
  print(result)