import heapq
def solution():    
    jewerly_bags.sort(key=lambda x : (x[0],-x[1]))

    heap=[]

    result=0
    for weight,priority in jewerly_bags:
        if priority != -1:
            heapq.heappush(heap,(-priority))
        else:
            if heap:
                result-=(heapq.heappop(heap))

    return result


if __name__== "__main__":
    N,K=0,0
    jewerly_bags=[]
    bags=[]

    with open("input1202.txt","r") as file:
        N,K=map(int,file.readline().split())
        for _ in range(N):
            weight,priority=map(int,file.readline().split())
            jewerly_bags.append((weight,priority))
        for _ in range(K): 
            jewerly_bags.append((int(file.readline()),-1))
    
    print(solution())