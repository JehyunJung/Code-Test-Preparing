from math import inf
def solution(start,count):
    global result
    if count==num//2:
        link=list(set(persons)-set(start))     
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
        if i not in start:
            solution(start+[i],count+1)


if __name__ == "__main__":
    num=0
    result=inf
    graph=[]
    with open("input14889.txt","r") as file:
        num=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(num)]
    persons=[i for i in range(num)]
    solution([],0)
    print(result)