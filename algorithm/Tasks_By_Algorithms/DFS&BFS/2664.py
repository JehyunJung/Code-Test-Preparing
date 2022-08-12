from collections import deque

def solution():
    visited=[False] * (n_vertex+1)
    queue=deque([(0,start)])

    while queue:
        cost,vertex=queue.popleft()

        if vertex == end:
            return cost
        
        if visited[vertex]:
            continue
        visited[vertex]=True

        for adj_vertex in graph[vertex]:
            queue.append((cost+1,adj_vertex))
    
    return -1


if __name__ == "__main__":
    n_vertex=0
    start,end=0,0
    n_edges=0
    graph=[]

    with open("input2664.txt","r") as file:
        n_vertex=int(file.readline())
        start,end=map(int,file.readline().split())
        n_edges=int(file.readline())
        graph=[[] for _ in range(n_vertex+1)]

        for _ in range(n_edges):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
    
    print(solution())