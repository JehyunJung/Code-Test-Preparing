from collections import deque
def solution():
    queue=deque()
    confused=False
    cycle=False
    sorted_list=[]
    

    for i in range(1,n_teams+1):
        if indegree[i]==0:
            queue.append(i)
 
    for _ in range(n_teams):
        if len(queue)==0:
            cycle=True
            break

        if len(queue)>=2:
            confused=True
            break

        vertex=queue.popleft()
        sorted_list.append(vertex)
        for adj_vertex in range(1,n_teams+1):
            if graph[vertex][adj_vertex]:
                indegree[adj_vertex]-=1

                if indegree[adj_vertex]==0:
                    queue.append(adj_vertex)

    if cycle or confused:
        print("IMPOSSIBLE")
    else:
        print(*sorted_list)
        

if __name__ =="__main__":
    testcases=0
    n_teams=0
    graph=[]
    indegree=[]

    with open("input45.txt","r") as file:
        testcases=int(file.readline())
        for _ in range(testcases):
            n_teams=int(file.readline())
            graph=[[False] * (n_teams+1) for _ in range(n_teams+1)]
            indegree=[0]*(n_teams+1)
            teams=list(map(int,file.readline().split()))
            
            for i in range(n_teams):
                for j in range(i+1,n_teams):
                    indegree[teams[j]]+=1
                    graph[teams[i]][teams[j]]=True
            
            n_changes=int(file.readline())
            for _ in range(n_changes):
                v1,v2=map(int,file.readline().split())
                if graph[v1][v2]:
                    indegree[v2]-=1
                    indegree[v1]+=1
                    graph[v1][v2]=False
                    graph[v2][v1]=True
                
                else:
                    indegree[v1]-=1
                    indegree[v2]+=1
                    graph[v2][v1]=False
                    graph[v1][v2]=True

            solution()
