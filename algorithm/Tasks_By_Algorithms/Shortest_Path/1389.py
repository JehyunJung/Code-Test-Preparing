from math import inf
def solution():
    for k in range(1,v+1):
        for i in range(1,v+1):
            for j in range(1,v+1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j]=graph[i][k] + graph[k][j]
    min_result=inf
    min_index=1
    for i in range(1,v+1):
        count=0
        for j in range(1,v+1):
            if i==j:
                continue
            count+=graph[i][j]
            
        if count < min_result:
            min_result=count
            min_index=i
    
    return min_index

if __name__ =="__main__":
    v,e=map(int,input().split());
    graph=[[inf] *(v+1) for _ in range(v+1)]
    
    for _ in range(e):
        v1,v2=map(int,input().split())
        graph[v1][v2]=1
        graph[v2][v1]=1
        
    print(solution())
