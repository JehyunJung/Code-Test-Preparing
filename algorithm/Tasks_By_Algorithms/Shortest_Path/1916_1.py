from math import inf
def solution(N,graph,start,end):
  distance=[inf] * (N+1)

  distance[start]=0
  
  for i in range(N):
    for vertex in range(1,N+1):
      for adj_vertex,weight in graph[vertex]:
        if distance[adj_vertex] > weight+ distance[vertex]:
          distance[adj_vertex] = weight+ distance[vertex]

          if i==N-1:
            return False

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