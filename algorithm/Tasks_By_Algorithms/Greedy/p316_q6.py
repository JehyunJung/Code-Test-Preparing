import heapq

food_times=[]
k=0

with open("input6.txt", "r") as file:
  food_times=list(map(int,file.readline().split()))
  k=int(file.readline())


def solution(food_times, k):
    answer = 0
    if sum(food_times) < k:
        return -1
    
    heap=[]
    for i in range(len(food_times)):
        heapq.heappush(heap,(food_times[i],i+1))
    
    eatingTimeSum=0
    prev=0
    length=len(heap)
    while eatingTimeSum + ((heap[0][0]-prev)*length) <= k:
        now=heapq.heappop(heap)[0]
        eatingTimeSum+=(now-prev)*length
        prev=now
        length-=1

    heap.sort(key=lambda x : x[1])
    answer=heap[(k-eatingTimeSum)%length][1]
    return answer

print(solution(food_times,k))
  