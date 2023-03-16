def heap_delete(heap,prev_index,new_index):
    global heap_index
    index=heap_index[prev_index]
    new_value=numbers[new_index]


    heap[index]=(new_value,new_index)
    #부모 노드보다 값이 작은 경우
    if index !=1 and new_value < heap[index//2][0]:
        while index !=1 and new_value < heap[index//2][0]:
            heap_index[heap[index//2][1]]=index
            heap[index//2],heap[index]=heap[index],heap[index//2]
            index//=2
    #부모 노드보다 값이 큰 경우
    else:

        child_index=index*2
        
        while child_index <=l:
            if child_index + 1 <=l and heap[child_index][0] > heap[child_index+1][0]:
                child_index+=1
            

            #부모 노드가 더 작은 경우 더 이상 변환 X
            if heap[child_index][0] >= heap[index][0]:
                break

            heap_index[heap[child_index][1]]=index  
            heap[index],heap[child_index]=heap[child_index],heap[index]
            
            index=child_index
        
    heap_index[new_index]=index

def heap_insert(heap,heap_size,number_index):
    global heap_index
    value=numbers[number_index]
    index=heap_size+1
    heap.append((value,number_index))
    while index !=1 and heap[index//2][0] > heap[index][0]:
        heap_index[heap[index//2][1]]=index
        heap[index//2],heap[index]=heap[index],heap[index//2]
        index//=2
    heap_index[number_index]=index

def solution():
    heap=[0]
    for i in range(l):
        heap_insert(heap,i,i)
        print(heap[1][0])

    for i in range(l,n):
        heap_delete(heap,i-l,i)
        print(heap[1][0])

if __name__ == "__main__":
    with open("input11003.txt","r") as file:
        n,l=map(int,file.readline().split())
        numbers=list(map(int,file.readline().split()))
    
    heap_index=[0]*n
    solution()