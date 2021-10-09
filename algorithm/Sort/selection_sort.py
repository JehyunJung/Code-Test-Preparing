def selection_Sort(n,data):
  for i in range(n):
    min_index=i
    
    for j in range(i+1,n):
      if data[j] < data[min_index]:
        min_index=j

    data[i],data[min_index]=data[min_index],data[i]


if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  selection_Sort(n,data)
  print("sorted_data:",data,sep="\t",end="\n")