from math import inf
def solution():
    for k in range(1,v+1):
        for i in range(1,v+1):
            for j in range(1,v+1):
                temp=graph[i][k]+graph[k][j]
                if temp < graph[i][j]:
                    graph[i][j]=temp

    
    for taskA, taskB in tasks:
        if graph[taskA][taskB] != inf:
            print(-1)
        elif graph[taskB][taskA] != inf:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    v,e=0,0
    graph=[]
    t=0
    tasks=[]
    with open("input1613.txt","r") as file:
        v,e=map(int,file.readline().split())
        graph=[[inf] * (v+1) for _ in range(v+1)]

        for _ in range(e):
            v1,v2=map(int,file.readline().split())
            graph[v1][v2]=1
        t=int(file.readline())
        tasks=[list(map(int,file.readline().split())) for _ in range(t)]

    solution()