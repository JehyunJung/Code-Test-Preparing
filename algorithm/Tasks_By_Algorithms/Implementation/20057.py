from math import floor
def move(cnt,move_dir,direction):
    global result,graph,current_row,current_col
    for _ in range(cnt+1):
        next_row=current_row+dy[move_dir]
        next_col=current_col+dx[move_dir]

        current_row,current_col=next_row,next_col

        #토네이도 끝까지 이동한 경우
        if current_row < 0 or current_col < 0:
            break

        spread_amount=0
        current_amount=graph[current_row][current_col]
        for y,x,r in direction:
            row=current_row+y
            col=current_col+x

            amount=int(current_amount*r)
            #만약 알파 칸에 대한 이동인 경우 비율칸으로 이동한 나머지의 모래양만큼이 이동하게 된다.
            if r==0:
                amount=(current_amount-spread_amount)

            #경계 밖으로 이동하게 되는 경우 
            if row < 0 or row >=num or col < 0 or col>=num:
                result+=amount
            #해당 칸으로 모래 이동
            else:
                graph[row][col]+=amount

            #이동하는 총 모래의 양
            spread_amount+=amount

        
    
def solution():
    left=[(-2,0,0.02),(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),
    (0,-2,0.05),
    (1,-1,0.1),(1,0,0.07),(1,1,0.01),
    (2,0,0.02),(0,-1,0)]

    right=[(x,-y,r) for x,y,r in left]
    up=[(y,x,r) for x,y,r in left]
    down=[(-y,x,r) for x,y,r in left]

    for i in range(num):
        #좌 + 하 이동
        if i % 2==0:
            move(i,3,left) 
            move(i,2,down)
        #우 + 상 이동
        else:
            move(i,1,right)
            move(i,0,up)
    
    return result

if __name__ == "__main__":
    num=0
    graph=[]
    result=0
    current_row,current_col =0,0
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input20057.txt","r") as file:
        num=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(num)]
    
    current_row,current_col = (num//2,num//2)
    print(solution())