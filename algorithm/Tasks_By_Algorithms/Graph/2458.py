from math import inf
def solution():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    
    
    
    for row in graph:
        print(*row)
                
    answer=0
    for i in range(n):
        graph[i][i]=0
        count=0
        for j in range(n):
            if graph[i][j] != inf or graph[j][i] != inf:
                count+=1
        
        if count==n:
            answer+=1
    
    print(answer)
            
      
if __name__ == "__main__":
    with open("input2458.txt","r") as file:
        n,m=map(int,file.readline().split())
        graph=[[inf] * n for _ in range(n)]

        for _ in range(m):
            v1,v2=map(int,file.readline().split())
            graph[v1-1][v2-1]=1
    
    solution()