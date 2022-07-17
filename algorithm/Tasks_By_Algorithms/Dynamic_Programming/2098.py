from math import inf
def solution():
    dp=[[-1] * (1<<n) for _ in range(n)]
    visited_all=(1<<n) -1
    def dfs(last,visited):
        
        if visited==visited_all:
            return distances[last][0] or inf

        if dp[last][visited]!=-1:
            return dp[last][visited]
        
        distance=inf
        for city in range(n):
            if visited & (1<<city) == 0 and distances[last][city] !=0:
                distance=min(distance,distances[last][city]+dfs(city,visited|(1<<city)))
        dp[last][visited]=distance
        return distance

    print(dfs(0,1))

if __name__ == "__main__":
    n=0
    distances=[]
    result=inf

    with open("input2098.txt","r") as file:
        n=int(file.readline())
        distances=[list(map(int,file.readline().split())) for _ in range(n)]
    
    solution()
    
    

        