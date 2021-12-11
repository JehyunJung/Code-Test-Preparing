from bisect import bisect_left
num=0
datas=[]

with open("input34.txt","r") as file:
  num=int(file.readline())
  datas=list(map(int,file.readline().split()))

datas.reverse()
sequence=[]
sequence.append(datas[0])
for i in range(1,num):
  if sequence[-1] < datas[i]:
    sequence.append(datas[i])
  else:
    index=bisect_left(sequence,datas[i])
    sequence[index]=datas[i]
    
print(num-len(sequence))