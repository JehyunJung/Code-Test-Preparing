from math import inf
def solution():
    prev_min_board=graph[0]
    prev_max_board=graph[0]

    for i in range(1,n):
        min_board=[inf]*3
        min_board[0]=min(prev_min_board[0]+graph[i][0],prev_min_board[1]+graph[i][0])
        min_board[1]=min(prev_min_board[0]+graph[i][1],prev_min_board[1]+graph[i][1],prev_min_board[2]+graph[i][1])
        min_board[2]=min(prev_min_board[1]+graph[i][2],prev_min_board[2]+graph[i][2])
        
        max_board=[0]*3
        max_board[0]=max(prev_max_board[0]+graph[i][0],prev_max_board[1]+graph[i][0])
        max_board[1]=max(prev_max_board[0]+graph[i][1],prev_max_board[1]+graph[i][1],prev_max_board[2]+graph[i][1])
        max_board[2]=max(prev_max_board[1]+graph[i][2],prev_max_board[2]+graph[i][2])

        prev_min_board=min_board
        prev_max_board=max_board
    

    print(max(prev_max_board),min(prev_min_board))

if __name__ == "__main__":
    n=0
    graph=[]

    with open("input2096.txt","r") as file:
        n=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]
    
    solution()