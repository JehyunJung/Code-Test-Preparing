from collections import deque
import sys

def solution():
    queue=deque()

    for i in range(1,n+1):
        if indegrees[i]==0:
            queue.append(i)

    top_order=[]
    while queue:
        vertex=queue.popleft()
        top_order.append(vertex)
        for adj_vertex in graph[vertex]:
            indegrees[adj_vertex]-=1

            if indegrees[adj_vertex] ==0:
                queue.append(adj_vertex)
    
    if len(top_order) != n:
        print(0)
    else:
        print("\n".join(map(str,top_order)))


if __name__ == "__main__":
    sys.stdin=open("input2623.txt", "r")
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    indegrees=[0]*(n+1)

    for _ in range(m):
        orders=list(map(int,input().split()))
        count=orders[0]

        for i in range(2,count+1):
            graph[orders[i-1]].append(orders[i])
            indegrees[orders[i]]+=1
    
    solution()
