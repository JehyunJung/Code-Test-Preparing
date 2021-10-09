def count_Sort(n,data,start,end):
  basket=[0]*(max(data)+1)
  index=0
  for i in range(n):
    basket[data[i]]+=1

  for i in range(len(basket)):
    target=basket[i]
    for j in range(target):
      data[index]=i
      index+=1

if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  count_Sort(n,data,0,n-1)
  print("sorted_data:",data,sep="\t",end="\n")