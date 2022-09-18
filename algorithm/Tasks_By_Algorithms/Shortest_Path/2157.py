from heapq import heappush,heappop

""" def solution():
    distance=[0]*(N+1)

    heap=[]
    #cost,vertex,path_length
    heappush(heap,(0,1,0))

    while heap:
        cost,vertex,length=heappop(heap)

        #마지막 노드이면 진행 X
        if vertex==N:
            continue

        #저장되어있는 만족도 보다 작으면 진행 X
        if distance[vertex] < cost:
            continue
        #거리가 M 이상 이면 더이상 진행 X
        if length > M:
            continue

        for adj_vertex, weight in graph[vertex].items():
            if distance[adj_vertex] > weight+cost:
                distance[adj_vertex] = weight+cost
                heappush(heap,(distance[adj_vertex],adj_vertex,length+1))
    return distance[N]*-1 """

def solution():
    dp=[[-1] * (M+1) for _ in range(N+1)]
    dp[1][1]=0
    
    for i in range(1,N+1):
        for j in range(1,M):
            if dp[i][j] == -1:
                continue
            for k in range(i+1,N+1):
                if graph[i][k]:
                    dp[k][j+1]=max(dp[k][j+1],dp[i][j]+graph[i][k])
    for row in graph:
        print(row)
    print(dp)
    return max(dp[N])
if __name__ == "__main__":
    N,M,K=0,0,0
    graph=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Shortest_Path\\input2157.txt","r") as file:
        N,M,K=map(int,file.readline().split())
        graph=[[0] * (N+1) for _ in range(N+1)]
        for _ in range(K):
            v1,v2,cost=map(int,file.readline().split())
            graph[v1][v2]=max(graph[v1][v2],cost)
    print(solution())
