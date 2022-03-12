from math import inf
from collections import deque
def solution(N,graph,start,end):
  distance=[inf] * (N+1)
  distance[start]=0
  queue=deque()
  
  for i in range(1,N+1):
    if indegree[i]==0:
      queue.append(i)
      
  while queue:
    vertex= queue.pop()
    
    for adj_vertex,weight in graph[vertex]:
      indegree[adj_vertex]-=1
      
      if indegree[adj_vertex] == 0:
        queue.append(adj_vertex)

      if distance[adj_vertex] > weight+ distance[vertex]:
        distance[adj_vertex] = weight+ distance[vertex]
      
  return distance[end]
  
if __name__ =="__main__":
  N,edges=0,0
  Graph=[]
  indegree=[]
  with open("input1916.txt","r") as file:
    N=int(file.readline())
    edges=int(file.readline())
    Graph=[[] for _ in range(N+1)]
    indegree=[0]*(N+1)
    for _ in range(edges):
      start,end,weight=map(int,file.readline().split())
      Graph[start].append((end,weight))
      indegree[end]+=1
    start,end=map(int,file.readline().split())

  print(solution(N,Graph,start,end))