from collections import deque
def solution():
    parents=[[0]*LENGTH for _ in range(n+1)]
    levels=[0]*(n+1)
    
    queue=deque([(1)])
    visited=[False]*(n+1)
    visited[1]=True

    while queue:
        vertex=queue.popleft()

        for adj_vertex in graph[vertex]:
            if visited[adj_vertex]:
                continue
            visited[adj_vertex]=True

            parents[adj_vertex][0]=vertex
            levels[adj_vertex]=levels[vertex]+1
            queue.append(adj_vertex)
    
    for i in range(1,LENGTH):
        for j in range(1,n+1):
            parents[j][i]=parents[parents[j][i-1]][i-1]
    

    for v1, v2 in queries:
        v1,v2=(v1,v2) if levels[v2]>levels[v1] else (v2,v1)

        for i in range(LENGTH-1,-1,-1):
            if levels[v2]-levels[v1]>=2**i:
                v2=parents[v2][i]

        if v1==v2:
            print(v1)
            continue

        for i in range(LENGTH-1,-1,-1):
            if parents[v1][i]!=parents[v2][i]:
                v1=parents[v1][i]
                v2=parents[v2][i]
        
        print(parents[v1][0])
        



if __name__ == "__main__":
    with open("input11437.txt","r") as file:
        n=int(file.readline())
        graph=[[] for _ in range(n+1)]
        LENGTH=21
        for _ in range(n-1):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        m=int(file.readline())
        queries=[list(map(int,file.readline().split())) for _ in range(m)]
    
    solution()