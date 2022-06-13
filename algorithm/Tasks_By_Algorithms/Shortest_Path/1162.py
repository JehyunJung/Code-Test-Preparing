import heapq
from math import inf

def solution():
    global result
    distance=[[inf] * (k+1) for _ in range(v+1)]
    distance[1][0]=0

    heap=[(0,1,0)]

    while heap:
        weight,vertex,pave=heapq.heappop(heap)

        if distance[vertex][pave]<weight:
            continue
        if vertex==v:
            result=min(result,weight)
        for adj_vertex,weight in graph[vertex]:
            cost=distance[vertex][pave]+weight
            if distance[adj_vertex][pave] > cost:
                distance[adj_vertex][pave]=cost
                heapq.heappush(heap,(cost,adj_vertex,pave))

            if pave+1<=k and distance[adj_vertex]>distance[vertex]:
                distance[adj_vertex][pave+1]=distance[vertex][pave]
                heapq.heappush(heap,(distance[vertex][pave],adj_vertex,pave+1))

    

        
if __name__ == "__main__":
    v,m,k=0,0,0
    graph=[] 
    result=inf
    with open("input1162.txt","r") as file:
        v,m,k=map(int,file.readline().split())
        graph=[[] for _ in range(v+1)]
        for _ in range(m):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1].append((v2,weight))
            graph[v2].append((v1,weight))


    solution()
    print(result)