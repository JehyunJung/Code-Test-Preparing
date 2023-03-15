from math import inf
from collections import deque
def solution():
    length=4
    parents=[[0] * length for _ in range(n+1)]
    min_max=[[[inf,-inf] for _ in range(length)] for _ in range(n+1)]

    queue=deque([1])
    visited=[False]*(n+1)
    levels=[0]*(n+1)
    visited[1]=True

    while queue:
        vertex=queue.popleft()

        for adj_vertex,weight in graph[vertex]:
            if visited[adj_vertex]:
                continue
            visited[adj_vertex]=True
            levels[adj_vertex]=levels[vertex]+1
            parents[adj_vertex][0]=vertex
            min_max[adj_vertex][0]=[weight,weight]
            queue.append(adj_vertex)

    for i in range(1,length):
        for j in range(1,n+1):
            near_parent=parents[j][i-1]
            parents[j][i]=parents[near_parent][i-1]
            values=[min_max[j][i-1][0],min_max[j][i-1][1],min_max[near_parent][i-1][0],min_max[near_parent][i-1][1]]
            min_max[j][i]=[min(values),max(values)]

    for v1,v2 in queries:
        v1,v2=(v1,v2) if levels[v1]<levels[v2] else (v2,v1)
        min_weight,max_weight=inf,-inf
        for i in range(length-1,-1,-1):
            if levels[v2]-levels[v1] >=2**i:
                values=[min_max[v2][i][0],min_max[v2][i][1]]
                min_weight=min(min_weight,min(values))
                max_weight=max(max_weight,max(values))
                v2=parents[v2][i]
        if v1==v2:
            print(min_weight,max_weight)
            continue

        for i in range(length-1,-1,-1):
            if parents[v1][i] != parents[v2][i]:
                values=[min_max[v1][i][0],min_max[v1][i][1],min_max[v2][i][0],min_max[v2][i][1]]
                min_weight=min(min_weight,min(values))
                max_weight=max(max_weight,max(values))

                v1=parents[v1][i]
                v2=parents[v2][i]

        values=[min_max[v1][0][0],min_max[v1][0][1],min_max[v2][0][0],min_max[v2][0][1]]
        min_weight=min(min_weight,min(values))
        max_weight=max(max_weight,max(values))
        print(min_weight,max_weight)
        
            

if __name__ == "__main__":
    with open("input3176.txt","r") as file:
        n=int(file.readline())
        graph=[[] for _ in range(n+1)]

        for _ in range(n-1):
            v1,v2,weight=map(int,file.readline().split())
            graph[v1].append((v2,weight))
            graph[v2].append((v1,weight))
        
        m=int(file.readline())
        queries=[list(map(int,file.readline().split())) for _ in range(m)]

    solution()
