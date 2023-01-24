from math import inf
from heapq import heappush,heappop
def solution():
    distances=[inf]*(d+1)
    heap=[(0,0)]
    distances[0]=0

    graph=[[] for _ in range(d+1)]

    for start,end,distance in shortcuts:
        graph[start].append((end,distance))

    while heap:
        cost,vertex=heappop(heap)

        if distances[vertex] < cost:
            continue
               
        distances[vertex]=cost

        if vertex >=d:
            continue

        for adj_vertex,weight in graph[vertex]:
            if adj_vertex > d:
                continue
            if distances[adj_vertex] > distances[vertex]+weight:
                distances[adj_vertex]=distances[vertex]+weight
                heappush(heap,(distances[adj_vertex],adj_vertex))

             
        heappush(heap,(distances[vertex]+1,vertex+1))

    print(distances[d])
if __name__ =="__main__":
    with open("input1446.txt","r") as file:
        n,d=map(int,file.readline().split())
        shortcuts=[list(map(int,file.readline().split())) for _ in range(n)]
    solution()