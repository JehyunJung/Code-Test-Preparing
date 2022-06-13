import heapq
from math import inf

def dijkstra(start):
    distance=[inf] * (v+1)
    distance[start]=0

    heap=[(0,start)]

    while heap:
        cost,vertex=heapq.heappop(heap)

        if cost>distance[vertex]:
            continue
            
        for adj_vertex,weight in graph[vertex]:
            cost=distance[vertex]+weight
            if distance[adj_vertex] > cost:
                distance[adj_vertex]=cost
                heapq.heappush(heap,(cost,adj_vertex))
    return distance

def solution():
    for i in range(1,v+1):
        distances.append(dijkstra(i))

    max_cost=0

    for i in range(1,v+1):
        max_cost=max(max_cost,distances[i][end]+distances[end][i])
    return max_cost
    
if __name__ == "__main__":
    v,e,end=0,0,0
    graph=[]
    distances=[]
    with open("input1238.txt","r") as file:
        v,e,end=map(int,file.readline().split())
        graph=[[] for _ in range(v+1)]
        for _ in range(e):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1].append((v2,weight))
        distances=[[]]
    print(solution())