def dfs(graph,path,previous_location,used_tickets):
    global answer
    if not answer and len(used_tickets) == len(tickets):
        answer=path
        return
    if not previous_location in graph:
        return
    for adj_node,ticket_index in graph[previous_location]:
        if ticket_index in used_tickets:
            continue
        dfs(graph,path+[adj_node],adj_node,used_tickets+[ticket_index])
    return
  
  
def solution(tickets):
    used_tickets=[]
    graph=dict()
    index=0
    for start,end in tickets:
        if start not in graph:
            graph[start]=[]
        graph[start].append((end,index))
        index+=1
        
    for node in graph:
        graph[node].sort()
    dfs(graph,["ICN"],"ICN",used_tickets)
  
    return answer
  
if __name__ == "__main__":
    num=0
    tickets=[]
    answer=[]
    with open("level3_3.txt","r") as file:
        num=int(file.readline())
        tickets=[list(map(str,file.readline().split())) for _ in range(num)]
    print(solution(tickets))