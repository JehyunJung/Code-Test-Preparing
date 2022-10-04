def dfs(vertex):
    global size,visited
    visited[vertex]=True

    for child in graph[vertex]:
        if visited[child]:
            continue
        size[vertex]+=dfs(child)
    
    return size[vertex]

if __name__ == "__main__":
    n_vertex,root,n_queries=0,0,0

    graph=[]
    visited=[]
    queries=[]
    with open("input15681.txt","r") as file:
        n_vertex,root,n_queries=map(int,file.readline().split())
        graph=[[] for _ in range(n_vertex+1)]
        visited=[False]*(n_vertex+1)
        for _ in range(n_vertex-1):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
        queries=[int(file.readline()) for _ in range(n_queries)]
    size=[1]*(n_vertex+1)

    for query in queries:
        print(size[query])

        

