def solution():
    papers.sort(reverse=True)
    dp=[1]*N
    print(papers)
    for i in range(1,N):
        for j in range(i):
            if papers[i][0] <= papers[j][0] and papers[i][1] <= papers[j][1]:
                dp[i]=max(dp[i],dp[j]+1)
    print(dp)
if __name__ == "__main__":
    N=0
    papers=[]

    with open("input2643.txt","r") as file:
        N=int(file.readline())
        for _ in range(N):
            v1,v2=map(int,file.readline().split())

            papers.append((max(v1,v2),min(v1,v2)))
    print(solution())