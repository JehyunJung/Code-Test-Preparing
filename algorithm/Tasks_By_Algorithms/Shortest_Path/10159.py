from math import inf
def solution():
    for k in range(1,n_vertex+1):
        for i in range(1, n_vertex+1):
            for j in range(1, n_vertex+1):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]


    for i in range(1,n_vertex+1):
        count=0
        for j in range(1,n_vertex+1):
            if i==j:
                continue
            elif graph[i][j] == inf and graph[j][i] == inf:
                count+=1
        print(count)
        
if __name__ == "__main__":
    n_vertex, n_edge=0,0
    graph=[]
    with open("input10159.txt","r") as file:
        n_vertex=int(file.readline())
        n_edge=int(file.readline())
        graph=[[inf]*(n_vertex+1) for _ in range(n_vertex+1)]
        for _ in range(n_edge):
            v1,v2=map(int,file.readline().split())
            graph[v1][v2]=1
    solution()