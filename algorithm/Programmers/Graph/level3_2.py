from math import inf
def solution(n, results):
    answer = 0
    distance=[[inf] *(n+1) for _ in range(n+1)]
        
    for start,end in results:
        distance[start][end]=1
       
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

        
    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if distance[i][j] != inf or distance[j][i]!=inf:
                count+=1
                
        if count==n-1:
            answer+=1
    
    return answer

if __name__ == "__main__":
    n_vertex,n_edges=0,0
    results=[]
    with open("level3_2.txt","r") as file:
        n_vertex,n_edges=map(int,file.readline().split())
        results=[list(map(int,file.readline().split())) for _ in range(n_edges)]
    print(solution(n_vertex,results))