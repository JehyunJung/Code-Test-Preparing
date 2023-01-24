from math import inf
def solution():

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and i!=j:
                graph[i][j]=inf

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j]=graph[i][k] + graph[k][j]
    
    for index in range(m-1):
        if graph[travel_route[index]][travel_route[index+1]] != inf or graph[travel_route[index+1]][travel_route[index]]!=inf:
            continue
        print("NO")
        break
    print("YES")

if __name__ == "__main__":
    with open("input1976.txt","r") as file:
        n=int(file.readline())
        m=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]
        travel_route=list(map(lambda x: int(x)-1,file.readline().split()))
    
    solution()