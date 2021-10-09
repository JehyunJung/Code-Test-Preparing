def quick_Sort(n,data,start,end):
  if n<=1:
    return data
  pivot=data[0]
  temp=data[1:]

  left=[x for x in temp if x <= pivot]
  right=[x for x in temp if x > pivot]

  return quick_Sort(len(left),left,0,len(left)-1) + [pivot]+ quick_Sort(len(right),right,0,len(right)-1)

if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  sorted_Data=quick_Sort(n,data,0,n-1)
  print("sorted_data:",sorted_Data,sep="\t",end="\n")