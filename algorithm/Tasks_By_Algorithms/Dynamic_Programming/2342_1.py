from math import inf
def initiate_transitions():
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
    return transitions
    
def solution(index, left,right):
    global dp
    if index == n:
        return 0
    if dp[index][left][right] != -1:
        return dp[index][left][right]

    next_move=moves[index]
    dp[index][left][right]=min(solution(index+1,left,next_move) + transitions[right][next_move], solution(index+1,next_move,right) + transitions[left][next_move])
    return dp[index][left][right]
            
if __name__ == "__main__":
    with open("input2342.txt","r") as file:
        moves=list(map(int,file.readline().split()))
    moves.pop()
    n=len(moves)

    transitions=initiate_transitions()

    dp=[[[-1] * 5 for _ in range(5)] for _ in range(n+1)]
    print(solution(0,0,0))