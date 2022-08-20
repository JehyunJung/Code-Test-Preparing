def solution():
    visited=[False] *(num+1)
    count=0
    for start_vertex in range(1,num+1):
        if visited[start_vertex]:
            continue        
        stack=[(start_vertex)]
        path=[]
        while stack:
            vertex=stack.pop(0)
            visited[vertex]=True
            path.append(vertex)
            adj_vertex=edges[vertex]
            if visited[adj_vertex]:
                if adj_vertex in path:
                    visited[vertex]=True
                    count+=len(path[path.index(adj_vertex):])
                break
            else:
                stack.append((adj_vertex))

    return num-count

if __name__ == "__main__":
    test_cases=0
    num=0
    edges=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Graph\\input9466.txt","r") as file:
        test_cases=int(file.readline())

        for _ in range(test_cases):
            num=int(file.readline())
            edges=[0]+list(map(int,file.readline().split())) 
            print(solution())