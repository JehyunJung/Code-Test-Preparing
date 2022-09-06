def destroy_marvels(blizard):
    global graph
    dir,speed=blizard
    row,col=((N+1)//2)-1,((N+1)//2)-1
    for i in range(1,speed+1):
        next_row=row+dy[dir-1]*i
        next_col=col+dx[dir-1]*i
        #구슬 파괴
        graph[next_row][next_col]=0

def extract_to_linear_list():
    temp=[]
    move_types=[[3,0],[2,1]]
    row,col=((N+1)//2)-1,((N+1)//2)-1
    for i in range(1,N+1):
        moves=move_types[i%2]
        for dir in moves:
            for _ in range(i):
                row+=dy[dir]
                col+=dx[dir]

                #범위를 벗어나게 되면 멈춘다.
                if row < 0 or row >=N or col < 0 or col>=N:
                    return temp

                #비어 있으면 앞에 있는 것을 땡겨온다.
                if graph[row][col] ==0:
                    continue
                    
                temp.append(graph[row][col])

def compose_to_doubly_list(linear_list):
    global graph
    new_graph=[[0] *N for _ in range(N)]
    move_types=[[3,0],[2,1]]
    row,col=((N+1)//2)-1,((N+1)//2)-1
    index=0
    #새로운 값들로 그래프를 초기화한다.
    for i in range(1,N+1):
        moves=move_types[i%2]
        for dir in moves:
            for _ in range(i):
                row+=dy[dir]
                col+=dx[dir]
                #모두 다 당겼으면 나오도록 한다.
                if index == len(linear_list):
                    graph=new_graph
                    return
                
                new_graph[row][col]=linear_list[index]
                index+=1

#구슬 폭발 함수                   
def explode_marvels(exploded_marvels,linear_list):
    new_list=[]
    length=len(linear_list)
    prev_index=linear_list[0]
    temp_list=[prev_index]
    count=1

    check=False
    index=1

    while index < length:
        #이전과 똑같은 번호를 가진 구슬이라면 temp 배열에 넣는다.
        if linear_list[index] == prev_index:
            temp_list.append(linear_list[index])
            count+=1
        #이전 칸과 다른 번호를 가지는 경우
        else:
            #같은 번호를 가진 구슬의 개수가 4개 이상인경우 -> 폭발시킨다.
            if count >= 4:
                check=True
                #번호에 따라, 폭발되는 구슬의 개수를 증가시킨다.
                exploded_marvels[prev_index]+=count
            #폭발되지 않는 구슬은 따로 빼놓는다.
            else:
                new_list.extend(temp_list)
            #다음 구슬에 대해서 계속 순회 진행
            prev_index=linear_list[index]
            temp_list=[prev_index]
            count=1

        index+=1
    if count>=4:
        check=True
        exploded_marvels[prev_index]+=count
    else:
        #마지막 구슬 목록을 추가시켜준다.
        new_list.extend(temp_list)
    return check, new_list

def change_marvels(linear_list):
    new_list=[]
    
    length=len(linear_list)
    prev_index=linear_list[0]
    count=1
    index=1
    while index < length:
        #같은 번호를 가진 구슬의 경우 개수 증가
        if linear_list[index] == prev_index:
            count+=1
        else:
            #같은 번호의 구슬에 대해, 몇개 반복했는지에 따라 -> A,B 그룹으로 변환해서 해당 값들을 추가
            new_list.append(count)  
            new_list.append(prev_index)
            prev_index=linear_list[index]
            count=1
        index+=1

    #혹 그래프의 길이를 능가하게 되는 경우 조절한다.
    if len(new_list) >= (N**2)-1:
        new_list=new_list[:(N**2)-1]

    return  new_list
def solution():
    exploded_marvels=[0] *4
    for blizard in blizards:
        #구슬의 파괴
        destroy_marvels(blizard)
        #구슬의 이동 -> 2차원 리스트를 1차원 리스트로 변환해서 진행하면 쉽게 연산을 수행하는 것이 가능하다.
        linear_list=extract_to_linear_list()

        #빈칸이 없을때까지 계속 반복
        while True:  
            #구슬의 폭발, 만약 폭발하지 않으면 종료
            result,linear_list=explode_marvels(exploded_marvels,linear_list)
            
            if len(linear_list)==0:
                return exploded_marvels[1] + 2*exploded_marvels[2] + 3*exploded_marvels[3]

            if not result:
                break
        #구슬의 벼화
        linear_list=change_marvels(linear_list)
        
        #1차원 리스트를 다시 2차원 리스트로 변환
        compose_to_doubly_list(linear_list) 
    
    return exploded_marvels[1] + 2*exploded_marvels[2] + 3*exploded_marvels[3]


if __name__ == "__main__":
    N,M=0,0
    graph=[]
    blizards=[]

    dy=[-1,1,0,0]
    dx=[0,0,-1,1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input21611.txt","r") as file:
        N,M=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(N)]
        blizards=[list(map(int,file.readline().split())) for _ in range(M)]
    
    print(solution())