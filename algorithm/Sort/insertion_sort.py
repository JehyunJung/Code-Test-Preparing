def insertion_Sort(n,data):
  for i in range(1,n):
    for j in range(i,0,-1):
      if data[j-1] > data[j]:
        data[j],data[j-1]=data[j-1],data[j]
      else:
        break  


if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  insertion_Sort(n,data)
  print("sorted_data:",data,sep="\t",end="\n")