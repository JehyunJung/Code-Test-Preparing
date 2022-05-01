def solution(y,x):
    global visited
    if y==h-1 and x==w-1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
      
    visited[y][x]=0

    for dir in range(4):
        new_y=y+dy[dir]
        new_x=x+dx[dir]
        
        if new_y < 0 or new_y >=h or new_x <0 or new_x>=w:
            continue
  
        if graph[y][x] <= graph[new_y][new_x]:
            continue
          
        visited[y][x]+=solution(new_y,new_x)    
      
    return visited[y][x]
    
if __name__ == "__main__":
    w,h=0,0
    graph=[]
    
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    with open("input1520.txt","r") as file:
        h,w=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(h)]
    visited=[[-1] * w for _ in range(h)]
    print(solution(0,0))