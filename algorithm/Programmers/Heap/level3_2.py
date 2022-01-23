import heapq
def solution(operations):
    answer = []
    min_heap=[]
    max_heap=[]
    
    for operation in operations:
        command,option=operation.split()
        option=int(option)
        if command =='I':
            heapq.heappush(min_heap,option)
            heapq.heappush(max_heap,-option)
        else:
            if len(min_heap)==0:
              continue
              
            elif option==1:
                heapq.heappop(max_heap)
                min_heap=[]
                for data in max_heap:
                    heapq.heappush(min_heap,-data)
            else:
                heapq.heappop(min_heap)
                max_heap=[]
                for data in min_heap:
                    heapq.heappush(max_heap,-data)

    if len(min_heap)>=1:
        answer.append(min_heap[0])
    else:
        answer.append(0)   
        
    if len(max_heap)>=1:
        answer.append(-max_heap[0])
    else:
        answer.append(0)
        
    return answer

if __name__ == "__main__":
  operations=[]
  n=0
  with open("level3_2.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      operations.append(file.readline().strip())
  print(operations)
  print(solution(operations))
  