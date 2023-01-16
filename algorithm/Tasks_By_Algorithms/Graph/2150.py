def dfs(graph,vertex):
    global dfs_stack   
    
    if visited[vertex]:
        return
    visited[vertex]=True
   
    for adj_vertex in graph[vertex]:
        dfs(graph,adj_vertex)

    dfs_stack.append(vertex)
    
def solution():
    global visited,dfs_stack
    #dfs 수행
    for vertex in range(1,n_vertex+1):
        if not visited[vertex]:
            dfs(graph,vertex)

    stack=dfs_stack[:]
    visited=[False]*(n_vertex+1)
    components=[]
    #역방향 그래프에 대한 dfs 수행을 통해 SCC을 찾는다.
    while stack:
        vertex=stack.pop()
        if visited[vertex]:
            continue

        dfs_stack=[]
        dfs(rev_graph,vertex)
        components.append(sorted(dfs_stack))
    
    components.sort()

    print(len(components))
    for component in components:
        for vertex in component:
            print(vertex,end=" ")
        print(-1)


if __name__ == "__main__":
    with open("input2150.txt","r") as file:
        n_vertex,n_edge=map(int,file.readline().split())
        graph=[[] for _ in range(n_vertex+1)]
        rev_graph=[[] for _ in range(n_vertex+1)]
        for _ in range(n_edge):
            src,des=map(int,file.readline().split())
            graph[src].append(des)
            rev_graph[des].append(src)
    dfs_stack=[]  
    visited=[False] * (n_vertex+1)
    solution()