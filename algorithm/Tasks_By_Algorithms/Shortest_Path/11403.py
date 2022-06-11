from math import inf
def distance_converter(option):
    if option:
        for i in range(n):
            for j in range(n):
                if graph[i][j]==0:
                    graph[i][j]=inf
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j]==inf:
                    graph[i][j]=0
                else:
                    graph[i][j]=1

def solution():

    distance_converter(True)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j]=graph[i][k] + graph[k][j]

    distance_converter(False)

    for i in range(n):
        print(*graph[i])
    

if __name__ =="__main__":
    n=0;
    graph=[]

    with open("input11403.txt","r") as file:
        n=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]

    solution()
