def solution(vertex):
    global dp

    for child in graph[vertex]:
        dp[vertex][1]+=solution(child)
        dp[vertex][0]+=dp[child][1]

    return min(dp[vertex])
    
if __name__ == "__main__":
    N=0
    graph=[]
    dp=[]
    with open("input2533.txt","r") as file:
        N=int(file.readline())
        graph=[[] for _ in range(N+1)]
        for _ in range(N-1):
            v1,v2=map(int,file.readline().split())
            graph[v1].append(v2)
    
    dp=[[0,1] for _ in range(N+1)]

    print(solution(1))