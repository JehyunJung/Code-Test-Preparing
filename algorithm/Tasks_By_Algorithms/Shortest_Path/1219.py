from math import inf
from collections import deque

def cycle_check(vertex):
    queue=deque([(vertex)])
    visited=[False]*(v)
    
    while queue:
        temp=queue.popleft()
        visited[temp]=True
        
        if temp==end:
            return True
        
        for adj_vertex in range(v):
            if temp != adj_vertex and not visited[adj_vertex] and graph[temp][adj_vertex] != inf:
                queue.append(adj_vertex)

    return False

def solution():
    for i in range(v):
        for j in range(v):
            if graph[i][j] != inf:
                graph[i][j] -=city_earnings[j]
    
    for times in range(v):
        for i in range(v):
            for j in range(v):
                if graph[i][j] != inf:

                    if distance[j] > distance[i]+graph[i][j]:
                        distance[j]=distance[i]+graph[i][j]

                        if times==v-1:
                            if cycle_check(j):
                                return False
    
    return True
            

if __name__ == "__main__":
    v,start,end,e=0,0,0,0
    graph=[]
    city_earnings=[]

    with open("input1219.txt","r") as file:
        v,start,end,e=map(int,file.readline().split())

        graph=[[inf] * v for _ in range(v)]

        for _ in range(e):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1][v2]=weight


        city_earnings=list(map(int,file.readline().split()))

    distance=[inf] *(v)
    distance[start]=-city_earnings[start]

    result=solution()
    print(result,distance)

    #무한히 돈을 많이 가지고 있을 수 있는 경우
    if not result:
        if distance[end]==inf:
            print("gg")
        else:
            print("Gee")

    #경로 존재
    else:
        if distance[end]==inf:
            print("gg")
        else:
            print(-distance[end])