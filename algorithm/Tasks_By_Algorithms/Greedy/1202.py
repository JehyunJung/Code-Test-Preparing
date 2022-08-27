from heapq import heappush,heappop
def solution():

    bags.sort()

    result=0
    candidates=[]
    for bag_weight in bags:
        while jewerly and bag_weight >= jewerly[0][0]:
            weight,priority=heappop(jewerly)
            heappush(candidates,(-priority))
        
        if candidates:
            result-=heappop(candidates)

    return result


if __name__== "__main__":
    N,K=0,0
    jewerly=[]
    bags=[]

    with open("input1202.txt","r") as file:
        N,K=map(int,file.readline().split())
        for _ in range(N):
            weight,priority=map(file.readline().split())
            heappush(jewerly,(weight,priority))
        bags=[int(file.readline()) for _ in range(K)]
    
    print(solution())