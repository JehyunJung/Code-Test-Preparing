
def solution():
    dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(num+1)]
 
    for i in range(1, 10):
        dp[1][i][1<<i] = 1
 
    for length in range(num):
        for last in range(10):
            for used in range(1024):
                if last < 9:
                    dp[length+1][last][used | (1<<last)] = (dp[length+1][last][used | (1<<last)] + dp[length][last+1][used]) % 1000000000
                if last > 0:
                    dp[length+1][last][used | (1<<last)] = (dp[length+1][last][used | (1<<last)] + dp[length][last-1][used]) % 1000000000
    
    return sum([dp[num][i][1023] for i in range(10)]) % 1000000000

if __name__ == "__main__":
    num=0

    with open("input1562.txt","r") as file:
        num=int(file.readline())
    print(solution())