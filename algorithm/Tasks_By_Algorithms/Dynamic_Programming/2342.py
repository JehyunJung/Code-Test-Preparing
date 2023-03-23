from math import inf
def solution():
    transitions=[[1]*5 for _ in range(5)]

    #이동 거리 비용 초기화
    for i in range(5):
        for j in range(5):
            if i==j:
                continue

            if i==0:
                transitions[i][j]=2
            
            elif abs(i-j) ==2:
                transitions[i][j]=4
            
            else:
                transitions[i][j]=3
    

    dp=[[[inf] *5 for _ in range(5)] for _ in range(n+1)]
    dp[0][0][0]=0

    for index in range(1,n+1):
        for left in range(5):
            for right in range(5):
                #같은 발이면 이동 X
                if index !=1 and left == right:
                    continue                
                next_move=moves[index-1] 

                #왼쪽을 움직이는 경우
                dp[index][next_move][right]=min(dp[index][next_move][right],dp[index-1][left][right]+transitions[left][next_move])

                #오른쪽을 움직이는 경우
                dp[index][left][next_move]=min(dp[index][left][next_move],dp[index-1][left][right]+transitions[right][next_move])
            



    min_distance=inf
    for left in range(5):
        for right in range(5):
            min_distance=min(min_distance,dp[n][left][right])

    print(min_distance)
            
if __name__ == "__main__":
    with open("input2342.txt","r") as file:
        moves=list(map(int,file.readline().split()))
    moves.pop()
    n=len(moves)
    solution()