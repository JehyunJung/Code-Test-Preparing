from heapq import heappush,heappop
def solution():
    left_heap,right_heap=[],[]
    left_count,right_count=0,0

    for index in range(n):
        data=datas[index]
        if left_count != right_count:
            heappush(right_heap,data)
            right_count+=1
        else:
            heappush(left_heap,-data)
            left_count+=1

        
        if right_heap and -left_heap[0] > right_heap[0]:
            left_data=-heappop(left_heap)
            right_data=heappop(right_heap)
            heappush(right_heap,left_data)
            heappush(left_heap,-right_data)
        
        print(-left_heap[0])   


   
if __name__ == "__main__":
    with open("input1655.txt","r") as file:
        n=int(file.readline())
        datas=[]

        for _ in range(n):
            datas.append(int(file.readline()))
    
    solution()