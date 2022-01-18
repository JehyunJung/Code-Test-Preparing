import heapq
from collections import deque
def solution(jobs):
    answer = 0
    candidate_jobs=[]
    
    heapq.heapify(candidate_jobs)
    jobs.sort()
    jobs=deque(jobs)
    job_length=len(jobs)
    time=0
    count=0
    
    while count< job_length:
        while jobs:
            temp=jobs.popleft()
            if temp[0] <= time:
                heapq.heappush(candidate_jobs,(temp[1],temp[0]))
            else:
                jobs.appendleft(temp)
                break
        if candidate_jobs:
            job=heapq.heappop(candidate_jobs)
            time+=job[0]
            answer+=time-job[1]
            count+=1
        else:
            time+=1
        
    answer//=job_length
    
    return answer

if __name__ == "__main__":
  n=0
  jobs=[]
  with open("level3_1.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      jobs.append(list(map(int,file.readline().split())))
  print(solution(jobs))
