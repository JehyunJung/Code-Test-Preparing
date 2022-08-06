from collections import deque
from copy import deepcopy

def solution():
    
    distance=deepcopy(weight)
    queue=deque()
    for i in range(1,n_vertex+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        vertex= queue.popleft()

        if vertex == target:
            break
        for adj_vertex in graph[vertex]:
            indegree[adj_vertex]-=1
            distance[adj_vertex-1]=max(distance[adj_vertex-1],distance[vertex-1]+weight[adj_vertex-1])

            if indegree[adj_vertex]==0:
                queue.append(adj_vertex)
        
        if target in queue:
            break
                
             
    return distance[target-1]

if __name__ == "__main__":
    n_vertex,n_rules=0,0
    weight=[]
    graph=[]
    target=0
    indegree=[]
    
    with open("input1005.txt","r") as file:
        n_vertex,n_rules=map(int,file.readline().split())
        weight=list(map(int,file.readline().split()))
        graph=[[] for _ in range(n_vertex+1)]
        indegree=[0]*(n_vertex+1)
        for _ in range(n_rules):
            start,end=map(int,file.readline().split())
            graph[start].append(end)
            indegree[end]+=1
        target=int(file.readline())
    print(solution())


