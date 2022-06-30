from math import inf
from itertools import combinations

def solution():
    persons=[i for i in range(num)]
    result=inf
    for combination in list(combinations(persons,num//2)):
        start=list(combination)
        link=list(set(persons)-set(combination))

        start_power=0
        link_power=0
        for i in range(num//2):
            for j in range(num//2):
                if i==j:
                    continue
                start_power+=graph[start[i]][start[j]]
                link_power+=graph[link[i]][link[j]]
        
        result=min(result,abs(start_power-link_power))


    print(result)
if __name__ == "__main__":
    num=0
    graph=[]
    with open("input14889.txt","r") as file:
        num=int(file.readline())
        graph=[list(map(int,file.readline().split())) for _ in range(num)]
    
    solution()