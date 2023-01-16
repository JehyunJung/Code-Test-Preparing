from math import inf
def dfs(vertex,path):
    global dp
    #모든 노드를 방문한 경우
    if path == all_visited:
        return graph[vertex][0] or inf

    #해당 노드에 이미 방문한 적이 있는 경우
    if dp[vertex][path] != inf:
        return dp[vertex][path]
    
    for adj_vertex in range(n_vertex):
        adj_vertex_bit=1<<adj_vertex  
        if path & adj_vertex_bit ==0 and graph[vertex][adj_vertex] !=0 :
            new_path=path | adj_vertex_bit
            dp[vertex][path]=min(dp[vertex][path], graph[vertex][adj_vertex] + dfs(adj_vertex,new_path))
    return dp[vertex][path]
    

if __name__ == "__main__":
    with open("input10971.txt","r") as file:
        n_vertex=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n_vertex)]
    
    dp=[[inf] * (1<<n_vertex) for _ in range(n_vertex)]
    all_visited=(1<<n_vertex)-1

    print(dfs(0,1))

    