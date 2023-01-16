def solution(vertex):
    visited[vertex]=True
    for child in graph[vertex]:
        if visited[child]:
            continue

        solution(child)
        dp[vertex][1]+=dp[child][0]
        dp[vertex][0]+=max(dp[child])

    return max(dp[vertex])

if __name__ == "__main__":
    with open("input1949.txt","r") as file:
        n=int(file.readline())
        peoples=list(map(int,file.readline().split()))
        graph=[[] for _ in range(n)]
        dp=[[0,peoples[i]] for i in range(n)]

        visited=[False] * n

        for i in range(n-1):
            v1,v2=map(lambda x: int(x)-1,file.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)
    
    result=solution(0)
    print(result)

