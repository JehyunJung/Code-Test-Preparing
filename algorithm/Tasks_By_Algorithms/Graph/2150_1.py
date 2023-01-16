def dfs(vertex):
    global dfs_stack,components,id,finished
    discovered[vertex]=id
    id+=1

    stack.append(vertex)
    parent=discovered[vertex]

    for adj_vertex in graph[vertex]:
        if discovered[adj_vertex] == -1:
            parent=min(parent,dfs(adj_vertex))
        elif not finished[adj_vertex]:
            parent=min(parent,discovered[adj_vertex])
    
    if parent==discovered[vertex]:
        component=[]
        while stack:
            temp=stack.pop()
            component.append(temp)
            finished[temp]=True
            if temp == vertex:
                break
        components.append(sorted(component))

    return parent


    
def solution():
    #dfs 수행
    for vertex in range(1,n_vertex+1):
        if discovered[vertex]==-1:
            dfs(vertex)
    
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
    id=1
    components=[]
    stack=[]
    discovered=[-1] * (n_vertex+1)
    finished=[False]*(n_vertex+1)

    solution()