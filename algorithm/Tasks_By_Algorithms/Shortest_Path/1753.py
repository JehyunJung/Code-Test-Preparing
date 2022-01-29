from math import inf
import heapq
def solution():
    distance=[inf]*(vertices+1)
    distance[start]=0

    heap=[]        
    heapq.heappush(heap,(0,start))
    
    while heap:
        weight,vertex=heapq.heappop(heap)
        if weight > distance[vertex]:
            continue
        for adj_vertex,cost in graph[vertex]:
            temp=distance[vertex]+cost
            if distance[adj_vertex] > temp:
                distance[adj_vertex]=temp
                heapq.heappush(heap,(temp,adj_vertex))

    return distance



if __name__ == "__main__":
  with open("input1753.txt","r") as file:
    vertices,edges=map(int,file.readline().split())
    start=int(file.readline())
    graph=[[] for _ in range(vertices+1)]
    for _ in range(edges):
      v1,v2,w=map(int,file.readline().split())
      graph[v1].append((v2,w))
  
  distance=solution()

  for adj_vertex in range(1,vertices+1):
    if distance[adj_vertex] == inf:
      print("INF")
    else:
      print(distance[adj_vertex])