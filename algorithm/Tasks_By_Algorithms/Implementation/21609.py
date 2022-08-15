from collections import deque

def rotate_counterclockwise():
    global graph
    temp=[[0] *num for _ in range(num)]

    for i in range(num):
        for j in range(num):
            temp[num-j-1][i]=graph[i][j]

    graph=temp

def remove_elements(component):
    #-2를 빈칸으로 표현
    for row, col in component:
        graph[row][col]=-2

def activate_gravity():
    for row in range(num-2,-1,-1):
        for col in range(num):
            if graph[row][col]==-1:
                continue

            temp_row=row +1
            target_row=row

            while temp_row < num:
                if graph[temp_row][col] !=-2:
                    break
                target_row=temp_row
                temp_row+=1

            graph[row][col],graph[target_row][col]=graph[target_row][col],graph[row][col]

def find_blockgroups():
    block_groups=[]
    visited=[[False]*num for _ in range(num)]
    for start_row in range(num):
        for start_col in range(num):
            if graph[start_row][start_col] < 1 or visited[start_row][start_col]:
                continue
            queue=deque([(start_row,start_col)])
            color=graph[start_row][start_col]
            rainbow_blocks=[]
            normal_blocks=[]

            while queue:
                row,col=queue.popleft()

                if visited[row][col]:
                    continue

                if graph[row][col]==0:
                    rainbow_blocks.append((row,col))
                else:
                    normal_blocks.append((row,col))

                visited[row][col]=True

                for dir in range(4):
                    next_row=row+dy[dir]
                    next_col=col+dx[dir]

                    if next_row < 0 or next_row >=num or next_col < 0 or next_col>=num:
                        continue
                    #색깔이 같지 않은 블록 중에서
                    if graph[next_row][next_col] != color:
                        #검정색이 블록이거나, 무지개 블록이 아닌 경우 포함하지 않는다.
                        if graph[next_row][next_col] == -1 or graph[next_row][next_col] != 0:
                            continue

                    queue.append((next_row,next_col))

            for row,col in rainbow_blocks:
                visited[row][col]=False
            components=normal_blocks+rainbow_blocks
            if len(components) < 2:
                continue

            normal_blocks.sort(key=lambda x: (x[0],x[1]))

            #크기, 무지개 수, 기준 블록, 블록그룹
            block_groups.append((len(components),len(rainbow_blocks),normal_blocks[0][0],normal_blocks[0][1],components))
            
    return block_groups

def print_graph():
    for row in range(num):
        print(graph[row])

def solution():
    count=0
    while True:
        #블록 그룹 찾기
        print("1. Print Graph")
        print_graph()
        block_groups=find_blockgroups()
        
        if len(block_groups) ==0 :
            break
        #블록 그룹 중에서 가장 큰 블록 그룹 , 무지개 수가 가장 많은 그룹, 기준 블록의 행/열이 가장 큰 블록 그룹
        block_groups.sort(key=lambda x: (-x[0],-x[1],-x[2],-x[3]))
        
        print("BlockGroups: ", block_groups)
        target_component=block_groups[0][4]
        print("Target component: ", target_component)
        count+= (len(target_component) ** 2)
        #해당 블록 그룹에 해당하는 블록 제거
        remove_elements(target_component)
        print("2. Removed BlockGroups")
        print_graph()

        #중력 작용
        activate_gravity()
        print("3. Activate Gravity")
        print_graph()
        #반시계 회전
        rotate_counterclockwise()
        print("4. Rotation")
        print_graph()
        #중력 작용
        activate_gravity()
        print("5.Activate Gravity")
        print_graph()

    return count   
if __name__ == "__main__":
    num,colors=0,0
    graph=[]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    with open("input21609.txt","r") as file:
        num,colors=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(num)]

    print(solution())