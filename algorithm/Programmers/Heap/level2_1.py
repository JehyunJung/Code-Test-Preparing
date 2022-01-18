import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >=2 :
        first=heapq.heappop(scoville)
        if first >=K:
            break
        second=heapq.heappop(scoville)
        
        heapq.heappush(scoville,first+second*2)
        answer+=1
    
    if scoville[0] < K:
        answer=-1
        
    return answer

if __name__ == "__main__":
  scoville=[]
  K=0
  with open("level2_1.txt","r") as file:
    K=int(file.readline())
    scoville=list(map(int,file.readline().split()))

  print(solution(scoville,K))