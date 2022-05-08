import heapq
from math import inf

def solution(n, edge):
    answer = 0
    heap=[]
    graph=[[] for _ in range(n+1)]
    distance=[inf] * (n+1)
    
    for start,end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    distance[1]=0
    heapq.heappush(heap,(0,1))
    max_distance=0
    
    while heap:
        cost,vertex=heapq.heappop(heap)
        temp=cost+1
        for adj_vertex in graph[vertex]:
            if distance[adj_vertex] > temp:
                distance[adj_vertex]=temp
                heapq.heappush(heap,(temp,adj_vertex))
                max_distance=max(max_distance,temp)
    
    answer=distance[1:].count(max_distance)
        
    
    return answer
if __name__ == "__main__":
    n_vertex,n_edges=0,0
    edge=[]
    with open("level3_1.txt","r") as file:
        n_vertex,n_edges=map(int,file.readline().split())
        edge=[list(map(int,file.readline().split())) for _ in range(n_edges)]
      
    print(solution(n_vertex,edge))
        