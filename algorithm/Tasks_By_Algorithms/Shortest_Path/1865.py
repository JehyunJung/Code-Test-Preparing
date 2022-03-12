from math import inf
def solution(graph,N):
    distance=[inf] * (N+1)
    distance[1]=0
    
    for i in range(N):
        for vertex in range(1,N+1):
            for adj_vertex,weight in graph[vertex]:
                if distance[adj_vertex] > distance[vertex] + weight:
                    distance[adj_vertex]=distance[vertex]+weight
                    
                    if i==N-1:
                        return True
    return False

if __name__ == "__main__":
    testcases=0
    N,edges,wormhalls=0,0,0
    graph=[]
    with open("input1865.txt","r") as file:
      testcases=int(file.readline())
      for _ in range(testcases):
        N,edges,wormhalls=map(int,file.readline().split())
        graph=[[] for _ in range(N+1)]
    
        for _ in range(edges):
            start,end,weight=map(int,file.readline().split())
            graph[start].append((end,weight))
            graph[end].append((start,weight))
            
        for _ in range(wormhalls):
            start,end,weight=map(int,file.readline().split())
            graph[start].append((end,-weight))
            
        if solution(graph,N):
            print("YES")
        else: 
            print("NO")