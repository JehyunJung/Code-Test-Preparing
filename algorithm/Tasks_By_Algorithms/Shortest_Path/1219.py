from math import inf
from collections import deque

def solution():
    distances=[inf] *(v)
    distances[start]=-city_earnings[start]

    for i in range(e):
        edges[i][2]-=city_earnings[edges[i][1]]

    cycle=False
    reachable=False
    for times in range(v):
        for v1,v2,cost in edges:
            cost=distances[v1]+cost
            if distances[v1]!=inf and distances[v2] > cost:
                distances[v2]=cost
                if times==v-1:
                    cycle=True
                    queue=deque([v2])
                    visited=[False]*(v)
                    
                    while queue:
                        vertex=queue.popleft()
                        visited[vertex]=True
                        
                        if vertex==end:
                            reachable=True
                        
                        for adj_vertex in graph[vertex]:
                            if not visited[adj_vertex]:
                                queue.append(adj_vertex)
    
    if distances[end]==inf:
        print("gg")
    else:
        if cycle and reachable:
            print("Gee")
        else:
            print(-distances[end])


if __name__ == "__main__":
    v,start,end,e=0,0,0,0
    graph=[]
    city_earnings=[]
    edges=[]
    with open("input1219.txt","r") as file:
        v,start,end,e=map(int,file.readline().split())

        graph=[[] * v for _ in range(v)]

        for _ in range(e):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1].append((v2))
            edges.append([v1,v2,weight])

        city_earnings=list(map(int,file.readline().split()))

    

    solution()
    
