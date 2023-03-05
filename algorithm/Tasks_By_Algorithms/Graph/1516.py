from collections import deque
from math import inf

def solution():
    distances=[0]*n
    graph=[[] for _ in range(n)]
    processing_time=[0]*n
    indegrees=[0]*(n)
    
    for vertex in range(n):
        processing_time[vertex]=edges[vertex][0]

        for adj_vertex in edges[vertex][1:]:
            if adj_vertex ==-1:
                break
            graph[adj_vertex-1].append(vertex)
        
            indegrees[vertex]+=1

    queue=deque()
    for vertex in range(n):
        if indegrees[vertex]==0:
            queue.append(vertex)
            distances[vertex]=processing_time[vertex]
    
    while queue:
        vertex=queue.popleft()
        for adj_vertex in graph[vertex]:
            distances[adj_vertex]=max(distances[adj_vertex],distances[vertex]+processing_time[adj_vertex])
            indegrees[adj_vertex]-=1

            if indegrees[adj_vertex]==0:
                queue.append(adj_vertex)
        
    
    for distance in distances:
        print(distance)

if __name__ == "__main__":
    with open("input1516.txt","r") as file:
        n=int(file.readline())
        edges=[list(map(int,file.readline().split())) for _ in range(n)]

    solution()