def move_clouds(clouds,dir,speed):
    visited=[[False] * N for _ in range(N)]
    for i in range(len(clouds)):
        cloud_row=clouds[i][0]
        cloud_col=clouds[i][1]

        cloud_row = (cloud_row+ dy[dir-1]*speed)%N
        cloud_col = (cloud_col+ dx[dir-1]*speed)%N
        visited[cloud_row][cloud_col]=True
        clouds[i]=[cloud_row,cloud_col]
    return visited
def increase_water(clouds):
    for row ,col in clouds:
        graph[row][col]+=1

def copy_water(clouds):
    for row,col in clouds:
        count=0
        for dir in range(1,8,2):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col>=N:
                continue

            if graph[next_row][next_col]!=0:
                count+=1
        
        graph[row][col]+=count

def new_clouds(clouds,visited):
    new_clouds=[]
    for row in range(N):
        for col in range(N):
            if graph[row][col] < 2:
                continue

            if not visited[row][col]:
                graph[row][col]-=2
                new_clouds.append((row,col))
    return new_clouds

def print_graph():
    print("GRAPH")
    for row in graph:
        print(row)
def solution():
    clouds=[[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

    for dir,speed in moves:
        visited=move_clouds(clouds,dir,speed)
        increase_water(clouds)
        copy_water(clouds)
        clouds=new_clouds(clouds,visited)

    count=0
    for row in graph:
        count+=sum(row)
    
    return count

if __name__ == "__main__":
    N,M=0,0
    graph=[]
    moves=[]
    dy=[0,-1,-1,-1,0,1,1,1]
    dx=[-1,-1,0,1,1,1,0,-1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input21610.txt","r") as file:
        N,M=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(N)]
        moves=[map(int,file.readline().split()) for _ in range(M)]
    
    print(solution())

