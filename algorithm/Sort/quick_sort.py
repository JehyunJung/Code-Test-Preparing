def quick_Sort(n,data,start,end):
  if start>=end:
    return
  pivot=start
  left=start+1
  right=end

  while left <= right:
    while left<=end and data[left] <= data[pivot]:
      left+=1
    while right> start and data[right] >= data[pivot]:
      right-=1
    if left>right:
      data[right],data[pivot]=data[pivot],data[right]
    else:
      data[left],data[right]=data[right],data[left]
  
  quick_Sort(n,data,start,right-1)
  quick_Sort(n,data,right+1,end)

if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  quick_Sort(n,data,0,n-1)
  print("sorted_data:",data,sep="\t",end="\n")