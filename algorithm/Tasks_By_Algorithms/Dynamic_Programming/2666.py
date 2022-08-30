from math import inf
def dfs(count,door1,door2):
    if count == n_movements:
        return 0

    next_door=movements[count]

    dp[next_door][door1][door2]=min(
        abs(next_door-door1) + dfs(count+1,next_door,door2),
        abs(next_door-door2) + dfs(count+1,door1,next_door)
    )

    return dp[next_door][door1][door2]  
if __name__ == "__main__":
    n_doors=0
    door1,door2=0,0
    n_movements=0
    movements=[]

    with open("input2666.txt","r") as file:
        n_doors=int(file.readline())
        door1,door2=map(int,file.readline().split())
        n_movements=int(file.readline())
        for _ in range(n_movements):
            movements.append(int(file.readline()))

    dp=[[[0] *(n_doors+1) for _ in range(n_doors+1)]for _ in range(n_doors+1)]
    print(dfs(0,door1,door2))