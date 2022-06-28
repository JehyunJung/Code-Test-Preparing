from heapq import heappush,heappop
def solution():

    if len(A) > len(B):
        print(-1)
        return

    heap=[]

    for data in A:
        heappush(heap,-1*data)

    
    result=[]
    removed_datas=[]
    index=0
    prev_index=index
    while True:
        data=heappop(heap)

        if -1*data <= B[index]:
            result.append(-1*data)
            index+=1

        else: 
            removed_datas.append(data)
        
        if prev_index != index:
            for data in removed_datas:
                heappush(heap,data)
            removed_datas=[]
            prev_index=index
            continue

        elif prev_index==index and len(removed_datas)==0:
            print(result)
            break

        else:
            print(-1)
            break        


if __name__ == "__main__":
    A,B=0,0
    B_length=0
    with open("input16943.txt","r") as file:
        A,B=map(str,file.readline().split())
    
    B=list(map(int,B))
    A=list(map(int,A))

    solution()
