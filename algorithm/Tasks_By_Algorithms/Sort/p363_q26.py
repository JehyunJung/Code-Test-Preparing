import heapq
n=0
data=[]

with open("input26.txt","r") as file:
  n=int(file.readline())
  for _ in range(n):
    heapq.heappush(data,int(file.readline()))

sub_sum=0
while len(data)>=2:
  min_data1,min_data2=heapq.heappop(data),heapq.heappop(data)
  min_data1+=min_data2
  sub_sum+=min_data1
  heapq.heappush(data,min_data1)

print(sub_sum)