def solution():
  start,end=1,data_array[-1]
  result=0

  while start <= end:
    mid=(start+end)//2
    count=0
    for data in data_array:
      temp=data
      while temp>mid:
          count+=1
          temp-=mid
    
    if count<n:
      end=mid-1
    else:
      result=max(result,mid)
      print(result,count)
      start=mid+1

  return result

if __name__ == "__main__":
  k,n=0,0
  data_array=[]

  with open("input1654.txt","r") as file:
    k,n=map(int,file.readline().split())
    for _ in range(k):
      data_array.append(int(file.readline()))
  
  data_array.sort()
  print(solution())