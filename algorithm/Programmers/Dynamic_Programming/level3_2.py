def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer=max(triangle[-1])
    return answer

if __name__ == "__main__":
    num=0
    triangle=[]
    with open("level3_2.txt","r") as file:
        num=int(file.readline())
        triangle=[list(map(int,file.readline().split())) for _ in range(num)]
    print(solution(triangle))
