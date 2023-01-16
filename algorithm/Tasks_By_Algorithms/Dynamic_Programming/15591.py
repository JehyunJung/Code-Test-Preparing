from heapq import heappush,heappop
from math import inf
from os.path import dirname,join

def dijkstra(start):
    heap=[(inf,start)]

    while heap:
        cost,vertex=heappop(heap)
        
        if cost > distances[start][vertex]:
            continue

        for adj_vertex,weight in graph[vertex]:
            
            #시작 노드는 배제
            if adj_vertex == start:
                continue

            if min(cost,weight) < distances[start][adj_vertex]:
                distances[start][adj_vertex]=min(cost,weight)
                heappush(heap,(distances[start][adj_vertex],adj_vertex))       

    
def solution():
    for i in range(1,N+1):
        dijkstra(i)
    
    for i in range(1,N+1):
        print(distances[i][1:])

if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input15591.txt')

    with open(filename,"r") as file:
        N,Q=map(int,file.readline().split())
        graph=[[] for _ in range(N+1)]

        for _ in range(N-1):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1].append((v2,weight))
            graph[v2].append((v1,weight))

        questions=[list(map(int,file.readline().split())) for _ in range(Q)]
    distances=[[inf] * (N+1) for _ in range(N+1)]
    solution()