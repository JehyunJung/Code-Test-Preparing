from math import inf
import heapq
def solution(N,graph,start,end):
  distance=[inf] * (N+1)
  heap=[]
  heapq.heappush(heap,(0,start))
  distance[start]=0
  
  while heap:
    cost,v=heapq.heappop(heap)

    if distance[v] < cost:
      continue
    
    for adj_v,weight in graph[v]:
      temp=cost+weight
      if distance[adj_v] > temp:
        distance[adj_v]=temp
        heapq.heappush(heap,(temp,adj_v))
        
  print(distance)
  return distance[end]
        
    
if __name__ =="__main__":
  N,edges=0,0
  Graph=[]
  with open("input1916.txt","r") as file:
    N=int(file.readline())
    edges=int(file.readline())
    Graph=[[] for _ in range(N+1)]
    for _ in range(edges):
      start,end,weight=map(int,file.readline().split())
      Graph[start].append((end,weight))
    start,end=map(int,file.readline().split())

  print(solution(N,Graph,start,end))