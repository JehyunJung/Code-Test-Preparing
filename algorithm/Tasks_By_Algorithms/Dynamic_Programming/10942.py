def solution():
    dp=[[0] * (n) for _ in range(n)]

    for num_length in range(n):
        for start in range(n-num_length):
            end=start+num_length
            if start==end:
                dp[start][end]=1
                continue
            if str[start]==str[end]:
                if num_length==1:
                    dp[start][end]=1
      
                if dp[start+1][end-1]:
                    dp[start][end]=1

    for i in range(n):
        print(dp[i])
      
    for start,end in questions:
        print(dp[start-1][end-1])
      
if __name__ == "__main__":
    n=0
    str=[]
    m=0
    questions=[]

    with open("input10942.txt","r") as file:
        n=int(file.readline())
        str=list(map(int,file.readline().split()))
        m=int(file.readline())

        questions=[list(map(int,file.readline().split())) for _ in range(m)]
    solution()