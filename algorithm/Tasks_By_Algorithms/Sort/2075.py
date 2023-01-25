from heapq import heapify, heappush, heappop

if __name__ == "__main__":
    with open("input2075.txt","r") as file:
        n=int(file.readline())
        heap=list(map(int,file.readline().split()))
        heapify(heap)

        for _ in range(n-1):
            datas=list(map(int,file.readline().split()))
            for data in datas:
                heappush(heap,data)
                heappop(heap)
        
        print(heap[0])