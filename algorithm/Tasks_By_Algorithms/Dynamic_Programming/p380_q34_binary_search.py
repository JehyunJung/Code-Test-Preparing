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
    for j in range(len(sequence)):
      if datas[i] < sequence[j]:
        sequence[j]=datas[i]
        break
print(num-len(sequence))