def solution(tickets):
    answer = []
    used_tickets=set()
    graph=dict()
    previous_location="ICN"
    index=0
    for start,end in tickets:
        if start not in graph:
            graph[start]=[]
        graph[start].append((end,index))
        index+=1
        
    for node in graph:
        graph[node].sort()
    
    while len(used_tickets) != len(tickets):
        print("Used Tickets=",used_tickets)
        print(previous_location,graph[previous_location])
        for adj_node,ticket_index in graph[previous_location]:
            if ticket_index in used_tickets:
                continue
            answer.append(previous_location)
            previous_location=adj_node
            used_tickets.add(ticket_index)
            break
    answer.append(previous_location)
    return answer
  
if __name__ == "__main__":
    num=0
    tickets=[]
    with open("level3_3.txt","r") as file:
        num=int(file.readline())
        tickets=[list(map(str,file.readline().split())) for _ in range(num)]
    print(solution(tickets))