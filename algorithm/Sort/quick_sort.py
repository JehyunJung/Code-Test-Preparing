def quick_Sort(n,data,start,end):
  if n <=1:
    return
  pivot=data[0] 


if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  quick_Sort(n,data)
  print("sorted_data:",data,sep="\t",end="\n")