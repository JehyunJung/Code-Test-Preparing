def solution():
  start,end=0,0
  count=0
  temp=0
  while end < len(datas):
    temp=sum(datas[start:end+1])
    if temp == sub_sum:
      start+=1
      count+=1
    
    elif temp < sub_sum:
      end+=1
    else:
      start+=1
  
  return count


if __name__ == "__main__":
  n,sub_sum=0,0
  datas=[]

  with open("input2003.txt","r") as file:
    n,sub_sum=map(int,file.readline().split())
    datas=list(map(int,file.readline().split()))

  print(solution())