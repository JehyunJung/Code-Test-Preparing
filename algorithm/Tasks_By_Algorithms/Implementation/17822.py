from collections import deque
def rotation(arr,option,move_range):
    #option==0 (clockwise)
    if option==0:
        for _ in range(move_range):
            arr.insert(0,arr.pop(-1))
    #option==1 (counter-clockwise)
    else:
        for _ in range(move_range):
            arr.append(arr.pop(0))

def bfs(visited,start_row,start_col,color):
    global check
    components=[]

    queue=deque([(start_row,start_col)])

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True

        components.append((row,col))

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]
            
            #인접한 부분 연결
            if next_col ==M:
                next_col=0
            if next_col == -1:
                next_col=M-1

            if next_row < 0 or next_row >=N:
                continue
            #같은 색깔에 대해서만 bfs 수행
            if plates[next_row][next_col] != color:
                continue
            queue.append((next_row,next_col))

    if len(components) <=1:
        return

    #component에 대해서 0처리
    for row,col in components:
        plates[row][col]=0
    
    check=True

def sum_of_plates():
    count=0
    sum_of_values=0

    for row in range(N):
        for col in range(M):
            if plates[row][col] ==0:
                continue
            count+=1
            sum_of_values+=plates[row][col]

    return sum_of_values,count
       
def print_plates():
    print("PLATES")
    for plate in plates:
        print(plate)

def solution():
    global check

    for i,dir,move_range in operations:
        for multiplier in range(1,(N//i)+1):
            rotation(plates[(i*multiplier)-1],dir,move_range)

        visited=[[0] * M for _ in range(N)]
        check=False
        for row in range(N):
            for col in range(M):
                if not visited[row][col] and plates[row][col]!=0:
                    bfs(visited,row,col,plates[row][col])
        
        #인접한 수가 없는 경우
        if not check:
            sum_of_values,count_of_value=sum_of_plates()
            #아무것도 남지 않은 경우에 대해서는 평균을 구할 수 없다.
            if count_of_value==0:
                continue
            avg_of_values=sum_of_values/count_of_value

            for row in range(N):
                for col in range(M):
                    if plates[row][col] ==0:
                        continue
                    if plates[row][col] < avg_of_values:
                        plates[row][col] +=1

                    elif plates[row][col] > avg_of_values:
                        plates[row][col] -=1

    sum_of_values,count_of_value=sum_of_plates()

    return sum_of_values

if __name__ == "__main__":
    N,M,T=0,0,0
    plates=[]
    operations=[]
    check=False

    with open("input17822.txt","r" ) as file:
        N,M,T=map(int,file.readline().split())
        plates=[list(map(int,file.readline().split())) for _ in range(N)]
        operations=[list(map(int,file.readline().split())) for _ in range(T)]
    
    print(solution())