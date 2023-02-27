from collections import deque
def solution():
    parents=[0] * (n+1)
    levels=[0]*(n+1)

    parents[1]=-1

    
    queue=deque([(1)])
    visited=[False]*(n+1)
    visited[1]=True

    while queue:
        vertex=queue.popleft()

        for adj_vertex in graph[vertex]:
            if visited[adj_vertex]:
                continue
            visited[adj_vertex]=True

            parents[adj_vertex]=vertex
            levels[adj_vertex]=levels[vertex]+1
            queue.append(adj_vertex)
    
    for v1, v2 in queries:
        while levels[v1] != levels[v2]:            
            if levels[v2] < levels[v1]:
                v1=parents[v1]
            
            else:
                v2=parents[v2]
        while v1 != v2:
            v1=parents[v1]
            v2=parents[v2]

        print(v1)


if __name__ == "__main__":
    with open("input11437.txt","r") as file:
        n=int(file.readline())
        graph=[[] for _ in range(n+1)]
        for _ in range(n-1):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        m=int(file.readline())
        queries=[list(map(int,file.readline().split())) for _ in range(m)]
    
    solution()