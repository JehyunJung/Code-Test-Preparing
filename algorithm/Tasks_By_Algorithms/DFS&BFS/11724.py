from collections import deque
def bfs(visited,start):
    queue=deque([(start)])
    while queue:
        vertex=queue.popleft()

        if visited[vertex]:
            continue

        visited[vertex]=True

        for adj_vertex in graph[vertex]:
            queue.append(adj_vertex)


def solution():
    visited=[False] * (n_vertex+1)
    count=0

    for i in range(1,n_vertex+1):
        if not visited[i]:
            bfs(visited,i)
            count+=1
    print(count)
if __name__ == "__main__":
    with open("input11724.txt","r") as file:
        n_vertex,n_edge=map(int,file.readline().split())
        graph=[[] for _ in range(n_vertex+1)]
        for _ in range(n_edge):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
    
    solution()