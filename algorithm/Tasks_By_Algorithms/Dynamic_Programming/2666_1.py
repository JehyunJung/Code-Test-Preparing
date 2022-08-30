from math import inf
def dfs(cnt,door1,door2,move_count):
    global min_result
    if cnt==n_movements:
        min_result=min(min_result,move_count)
        return
    next_door=movements[cnt]
    dfs(cnt+1, next_door,door2,move_count+abs(next_door-door1))
    dfs(cnt+1, door1,next_door,move_count+abs(next_door-door2))


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

    min_result=inf
    dfs(0,door1,door2,0)
    print(min_result)