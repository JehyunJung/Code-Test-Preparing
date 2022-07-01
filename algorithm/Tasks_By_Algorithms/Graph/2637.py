from collections import deque
def solution():
    basic_block_types=list(set([i for i in range(1,n_blocks+1)])-set(mid_block_types))

    basic_block_types.sort()
    mid_block_types.sort()   

    block_map=[[0] *(n_blocks+1) for i in range(n_blocks+1)]


    queue=deque()

    for i in range(1,n_blocks+1):
        if indegree[i]==0:
            queue.append(i)
    
    while queue:
        vertex=queue.popleft()

        for adj_vertex,cost in graph[vertex]:
            indegree[adj_vertex]-=1
            if vertex in basic_block_types:
                block_map[adj_vertex][vertex]+=cost
            else:
                for block in basic_block_types:
                    block_map[adj_vertex][block]+=(cost*block_map[vertex][block])

            if indegree[adj_vertex]==0:
                queue.append(adj_vertex)

    for basic_block in basic_block_types:
        print(basic_block,block_map[n_blocks][basic_block])

if __name__ == "__main__":
    n_blocks=0
    n_relations=0
    relations=[]
    indegree=[]
    graph=[]
    mid_block_types=[]
    with open("input2637.txt","r") as file:
        n_blocks=int(file.readline())

        indegree=[0 for _ in range(n_blocks+1)]
        graph=[[] for _ in range(n_blocks+1)]

        n_relations=int(file.readline())

        for _ in range(n_relations):
            end,start,counts=list(map(int,file.readline().split()))
            indegree[end]+=1
            graph[start].append((end,counts))
            mid_block_types.append(end)

     
    solution()
