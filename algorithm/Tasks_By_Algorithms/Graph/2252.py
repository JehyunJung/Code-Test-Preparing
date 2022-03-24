from collections import deque
def solution():
    queue=deque()
    ans=[]
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        vertex=queue.pop()
        ans.append(vertex)
        for adj_vertex in graph[vertex]:
            indegree[adj_vertex]-=1
            
            if indegree[adj_vertex]==0:
                queue.append(adj_vertex)
              
    print(*ans)
if __name__ == "__main__":
    N,m=0,0
    graph=[]
    indegree=[]
    with open("input2252.txt","r") as file:
      N,m=map(int,file.readline().split())
      graph=[[] for _ in range(N+1)]
      indegree=[0 for _ in range(N+1)]
      for _ in range(m):
        v1,v2=map(int,file.readline().split())
        graph[v1].append(v2)
        indegree[v2]+=1
    solution()
        