def block_move(graph,locations,type):
    if type==1:
        row,col=locations[0]
    
        #move to green
        while row < 9 and graph[row+1][col] ==0:
            row+=1
        graph[row][col]=1

        #move to blue
        row,col=locations[0]
        while col < 9 and graph[row][col+1] ==0:
            col+=1
        graph[row][col]=1
    
    #위치 좌표가 2개인 경우
    else:
        row1,col1=locations[0]
        row2,col2=locations[1]

        #move to green
        while row1 < 9 and row2 <9 and graph[row1+1][col1] ==0 and graph[row2+1][col2] ==0:
            row1+=1
            row2+=1
        graph[row1][col1]=1
        graph[row2][col2]=1

        row1,col1=locations[0]
        row2,col2=locations[1]

        #move to blue
        while col1 < 9 and col2 <9 and graph[row1][col1+1] ==0 and graph[row2][col2+1] ==0:
            col1+=1
            col2+=1
        graph[row1][col1]=1
        graph[row2][col2]=1
  

def check_green(graph):
    erase_count=0
    for row in range(6,10):
        count=0
        for col in range(4):
            if graph[row][col]==1:
                count+=1
        if count==4:
            move_rows(graph,row)
            erase_count+=1
    
    return erase_count

def check_blue(graph):
    erase_count=0
    for col in range(6,10):
        count=0
        for row in range(4):
            if graph[row][col]==1:
                count+=1
        if count==4:
            move_cols(graph,col)
            erase_count+=1
    
    return erase_count


#green area
def check_light_green(graph):
    for row in [4,5]:
        for col in range(4):
            if graph[row][col]:
                move_rows(graph,9)
                break
#blue area
def check_light_blue(graph):
    for col in [4,5]:
        for row in range(4):
            if graph[row][col]==1:
                move_cols(graph,9)
                break

def move_rows(graph,start_row):
    for row in range(start_row,3,-1):
        for col in range(4):
            graph[row][col]=graph[row-1][col]

    for col in range(4):
        graph[4][col]=0


def move_cols(graph,start_col):
    for col in range(start_col,3,-1):
        for row in range(4):
            graph[row][col]=graph[row][col-1]
    
    for row in range(4):
        graph[row][4]=0        


def solution():
    graph=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    result=0
    for t,row,col in blocks:
        locations=[(row,col)]
        if t==2:
            locations.append((row,col+1))
        elif t==3:
            locations.append((row+1,col))
        
        block_move(graph,locations,t)

        #초록색 영역에서 행이 가득 차있는지 여부 판단
        result+=check_green(graph)


        #파란색 영역에서 열이 가득 차있는지 여부 판단
        result+=check_blue(graph)

        #연한 초록 부분에 블록이 있는지 여부 조사
        check_light_green(graph)
       

        #연한 파란 부분에 블록이 있는지 여부 조사
        check_light_blue(graph)


    #초록색 칸과, 파란색 칸에 블록이 들어있는 칸의 개수
    count=64
    for row in graph:
        count-=row.count(0)
    
    print(result)
    print(count)

if __name__ == "__main__":
    n=0
    blocks=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input20061.txt","r") as file:
        n=int(file.readline())
        blocks=[list(map(int,file.readline().split())) for _ in range(n)]

    solution()