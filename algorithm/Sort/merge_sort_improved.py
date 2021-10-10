def merge_Sort(data):
  if len(data)<=1:
    return data
  mid=len(data)//2

  left=merge_Sort(data[:mid])
  right=merge_Sort(data[mid:])
  return merge(left,right)
  
def merge(left,right):
  i,j=0,0
  temp=[]
  while i<len(left) and j<len(right):
    if left[i] <= right[j]:
      temp.append(left[i])
      i+=1
    else:
      temp.append(right[j])
      j+=1

  while i<len(left):
    temp.append(left[i])  
    i+=1

  while j<len(right):
    temp.append(right[j])
    j+=1

  return temp
    

if __name__ =="__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))

  print("unsorted_data:",data,sep="\t",end="\n")
  sorted_data=merge_Sort(data)
  print("sorted_data:",sorted_data,sep="\t",end="\n")