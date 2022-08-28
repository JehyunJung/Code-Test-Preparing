def move_fireball(graph):
    temp_graph=[[[] for _ in range(N)]for _ in range(N)]

    for row in range(N):
        for col in range(N):
            #파이어볼이 들어있지 않은 경우
            if len(graph[row][col])==0:
                continue
            for mass,speed,direction in graph[row][col]:
                #각각의 행/열은 처음과 끝이 연결되어 있기 때문
                next_row=(row+dy[direction]*speed)%N
                next_col=(col+dx[direction]*speed)%N


                temp_graph[next_row][next_col].append((mass,speed,direction))
    
    #새로운 그래프를 기존의 그래프로 설정
    return temp_graph

def fireball_fusion(graph):
    for row in range(N):
        for col in range(N):
            fireball_count=len(graph[row][col])
            #파이어볼이 들어있지 않은 경우
            if fireball_count<=1:
                continue
            sum_mass=0
            even_directions=False
            odd_directions=False
            sum_speed=0
            
            for mass,speed,direction in graph[row][col]:
                sum_mass+=mass
                sum_speed+=speed
                
                if direction % 2==0:
                    even_directions=True
                else:
                    odd_directions=True
            
            divided_mass=sum_mass//5
            divided_speed=sum_speed//fireball_count

            graph[row][col]=[]

            #질량이 0이 되는 경우 소멸시킨다.
            if divided_mass==0:
                continue
            #방향이 모두 짝수 이거나, 홀수 인경우
            if (odd_directions & even_directions) == False:
                for i in range(4):
                    graph[row][col].append((divided_mass,divided_speed,2*i))
            
            else:
                for i in range(4):
                    graph[row][col].append((divided_mass,divided_speed,2*i+1))
              

def solution():
    graph=[[[] for _ in range(N)]for _ in range(N)]

     #초기 파이어볼 추가
    for row,col,mass,speed,direction in fireballs:
        graph[row-1][col-1].append((mass,speed,direction))

    
     
    for _ in range(K):
        graph=move_fireball(graph)
        fireball_fusion(graph) 
    
    sum_of_fireball_mass=0

    for row in range(N):
        for col in range(N):
            #파이어볼이 들어있지 않은 경우
            if len(graph[row][col])==0:
                continue
            for mass,speed,direction in graph[row][col]:
                sum_of_fireball_mass+=mass
    
    return sum_of_fireball_mass

if __name__ == "__main__":
    N,M,K=0,0,0
    fireballs=[]

    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,1,1,1,0,-1,-1,-1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input20056.txt","r") as file:
        N,M,K=map(int,file.readline().split())
        fireballs=[list(map(int,file.readline().split())) for _ in range(M)]
    
    print(solution())
