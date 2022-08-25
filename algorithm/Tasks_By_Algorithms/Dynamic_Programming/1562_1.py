
def solution():
    dp = [[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(num+1)]
 
    for i in range(1, 10):
        dp[1][i][i][i] = 1
 
    for length in range(num):
        for start in range(10):
            for end in range(10):
                for last in range(10):
                    if last > end:
                        dp[length+1][start][last][last] = (dp[length+1][start][last][last] + dp[length][start][end][last]) % 1000000000
                    elif last < start:
                        dp[length+1][last][end][last] = (dp[length+1][last][end][last] + dp[length][start][end][last]) % 1000000000
                    else:
                        dp[length+1][start][end][last] = (dp[length+1][start][end][last] + dp[length][start][end][last]) % 1000000000
    
    return sum([dp[num][0][9][i] for i in range(10)]) % 1000000000

if __name__ == "__main__":
    num=0

    with open("input1562.txt","r") as file:
        num=int(file.readline())
    print(solution())