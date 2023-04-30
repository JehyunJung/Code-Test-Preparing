from heapq import heappush, heappop
import sys

def solution():
    classes.sort(key=lambda x: x[0])
    heap=[]

    #첫 경우 삽입
    heappush(heap,classes[0][1])

    heapsize=1
    max_heapsize=1

    for start,end in classes[1:]:

        #만일 끝난 교실이 있는 경우
        if heap[0] <=start:
            heappop(heap)
            heapsize-=1

        #해당 수업 추가
        heappush(heap,end)    
        heapsize+=1    
        max_heapsize=max(max_heapsize,heapsize)
    
    print(max_heapsize)

if __name__ == "__main__":
    sys.stdin=open("input11000.txt","r")
    N=int(input())
    classes=[list(map(int,input().split())) for _ in range(N)]
    solution()