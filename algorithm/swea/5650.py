from collections import deque,defaultdict

def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    change_dir=[
        [],
        [2,3,1,0],
        [1,3,0,2],
        [3,2,0,1],
        [2,0,3,1],
        [2,3,0,1]
    ]
    worm_halls=defaultdict(list)
    start_positions=[]
    max_score=0
    for row in range(1,num+1):
        for col in range(1,num+1):
            #웜홀 파악
            if graph[row][col] >5:
                index=graph[row][col]
                worm_halls[index].append((row,col))
            #시작 가능 위치 파악
            if graph[row][col] ==0:
                start_positions.append((row,col))

    worms=dict()

    for v1,v2 in worm_halls.values():
        worms[v1]=v2
        worms[v2]=v1

    for start_row,start_col in start_positions:
        for start_dir in range(4):
            row,col,dir,score=start_row,start_col,start_dir,0
            while True:
                row,col=row+dy[dir],col+dx[dir]

                if row==start_row and col==start_col or graph[row][col]==-1:
                    max_score=max(max_score,score)
                    break
                    
                elif 1<=graph[row][col]<=5:
                    dir=change_dir[graph[row][col]][dir]
                    score+=1

                elif graph[row][col]>=6:
                    worm_index=graph[row][col]
                    row,col=worms[(row,col)]

    return max_score

if __name__== "__main__":
    num=0
    graph=[]
    test_cases=int(input())
    for i in range(test_cases):
        num=int(input())
        graph=[[5]*(num+2)]
        for _ in range(num):
        	graph.append([5]+list(map(int,input().split()))+[5])
        graph.append([5]*(num+2))
        print("#{} {}".format(i+1,solution()))

    
    