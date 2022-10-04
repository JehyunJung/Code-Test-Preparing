from math import inf
def solution():
    path=[-1] * (n+2)
    dp=[inf] * (n+2)

    dp[0]=0
    for i in range(1,n+2):
        distance=0
        for j in range(i-1,-1,-1):
            distance+=distances[j]

            if distance >max_distance:
                break

            if dp[j]+repair_times[i-1] < dp[i]:
                path[i]=j
                dp[i]=dp[j]+repair_times[i-1]

    
    last_location=n+1
    paths=[]
    while last_location !=0:
        if last_location != n+1:
            paths.append(last_location)
        last_location=path[last_location]
    paths=paths[::-1]
    print(dp[-1])
    print(len(paths))
    print(*paths)
    #print(*[])
    

if __name__ == "__main__":
    max_distance=0
    n=0
    distances=[]
    repair_times=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Dynamic_Programming\\input2651.txt","r") as file:
        max_distance=int(file.readline())
        n=int(file.readline())
        distances=list(map(int,file.readline().split()))
        repair_times=list(map(int,file.readline().split()))
    repair_times.append(0)
    solution()