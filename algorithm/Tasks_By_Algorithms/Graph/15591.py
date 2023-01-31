from collections import deque
from math import inf
def bfs(start,k):
    visited=[False] * (n+1)
    visited[start]=True

    queue=deque([(start,inf)])
    count=0
    while queue:
        vertex,cost=queue.popleft()

        for adj_vertex,new_cost in graph[vertex]:
            temp_cost=min(cost,new_cost)
            if not visited[adj_vertex] and temp_cost >=k:
                count+=1
                queue.append((adj_vertex,temp_cost))
                visited[adj_vertex]=True
    return count

def solution():
    for k,v in questions:
        print(bfs(v,k))

if __name__ == "__main__":
    with open("input15591.txt","r") as file:
        n,q=map(int,file.readline().split())
        graph=[[] for _ in range(n+1)]

        for _ in range(n-1):
            v1,v2,cost=map(int,file.readline().split())
            graph[v1].append((v2,cost))
            graph[v2].append((v1,cost))
    
        questions=[list(map(int,file.readline().split())) for _ in range(q)]
    solution()