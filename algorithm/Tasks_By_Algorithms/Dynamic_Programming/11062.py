import sys
def solution(turn,left,right):
    if left > right:
        return 0
    if dp[left][right] != 0:
        return dp[left][right]
    
    #근우 차례인 경우
    if turn == 0:
        max_score=max(solution(1-turn,left+1,right)+cards[left],solution(1-turn,left,right-1)+cards[right])
        dp[left][right]=max_score
    #명우 차례인 경우
    else:
        min_score=min(solution(1-turn,left+1,right),solution(1-turn,left,right-1))
        dp[left][right]=min_score
    
    return dp[left][right]



if __name__ == '__main__':
    sys.stdin=open("input11062.txt","r")
    n_testcases=int(input())
    for i in range(n_testcases):
        n=int(input())
        cards=list(map(int,input().split()))
        dp=[[0] * n for _ in range(n)]
        print(solution(0,0,n-1))