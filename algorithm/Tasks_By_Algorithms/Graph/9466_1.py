def dfs(v,visited,path):
    global cycles
    visited[v]=True
    adj_vertex=edges[v]

    path.append(v)

    if visited[adj_vertex]:
        if adj_vertex in path:
            cycles+=[path[path.index(adj_vertex):]]
        return
    else:
        dfs(adj_vertex,visited,path)

def solution():
    visited=[False] * (num+1)
    for i in range(1,num+1):
        if visited[i]:
            continue
        dfs(i,visited,[])
    count=0
    for cycle in cycles:
        count+=len(cycle)
    return num-count


if __name__ == "__main__":
    test_cases=0
    num=0
    edges=[]
    cycles=[]
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Graph\\input9466.txt","r") as file:
        test_cases=int(file.readline())

        for _ in range(test_cases):
            num=int(file.readline())
            edges=[0]+list(map(int,file.readline().split()))
            cycles=[]
            print(solution())