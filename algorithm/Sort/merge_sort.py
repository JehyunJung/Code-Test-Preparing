def merge_Sort(n,data,start,end):
  if start>=end:
    return
  mid=(start+end)//2
  merge_Sort(n,data,start,mid)
  merge_Sort(n,data,mid+1,end)
  merge(data,start,end)
  
def merge(data,start,end):
  mid=(start+end)//2
  i,j=start,mid+1
  temp=[]

  while i<=mid and j<=end:
    if data[i] <= data[j]:
      temp.append(data[i])
      i+=1
    else:
      temp.append(data[j])
      j+=1
  while i<=mid:
    temp.append(data[i])
    i+=1
  while j<=end:
    temp.append(data[j])
    j+=1
  k=0
  for i in range(start,end+1):
    data[i]=temp[k]
    k+=1
    

if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  merge_Sort(n,data,0,n-1)
  print("sorted_data:",data,sep="\t",end="\n")