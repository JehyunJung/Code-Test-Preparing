from math import inf
def solution(count):
    global result
    if count==num//2:
        start=[]
        link=[]
        for i in range(num):
            if team[i]==0:
                start.append(i)
            else:
                link.append(i) 
        start_power=0
        link_power=0
        for i in range(num//2):
            for j in range(num//2):
                if i==j:
                    continue
                start_power+=graph[start[i]][start[j]]
                link_power+=graph[link[i]][link[j]]
        result=min(result,abs(start_power-link_power))

    for i in range(num):
        if team[i]!=1:
            team[i]=1
            solution(count+1)
            team[i]=0


if __name__ == "__main__":
    num=0
    result=inf
    graph=[]
    
    with open("input14889.txt","r") as file:
        num=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(num)]
    team=[0 for i in range(num)]
    solution(0)
    print(result)