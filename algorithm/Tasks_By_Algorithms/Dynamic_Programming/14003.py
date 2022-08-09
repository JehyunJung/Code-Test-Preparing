from bisect import bisect_left
with open("input14003.txt","r") as file:
  num=int(file.readline())
  sequence=list(map(int,file.readline().split()))

L=[sequence[0]]

for i in range(1,num):
    if L[-1] < sequence[i]:
        L.append(sequence[i])
    else:
        L[bisect_left(L,sequence[i])]=sequence[i]
print(len(L))
print(*L)