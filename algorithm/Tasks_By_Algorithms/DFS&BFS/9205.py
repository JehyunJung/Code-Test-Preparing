from collections import deque
def solution():
    start_row,start_col=locations[0]
    end_row,end_col=locations[-1]

    visited={}

    for location in locations:
        visited[location]=False

    queue=deque([(start_row,start_col)])

    while queue:
        row,col=queue.popleft()

        if row == end_row and col == end_col:
            return "happy"
        
        if visited[(row,col)]:
            continue
    
        visited[(row,col)]=True

        for next_row,next_col in locations:
            if visited[(next_row,next_col)]:
                continue
            if abs(next_row - row + next_col - col) <= 1000:
                queue.append((next_row,next_col))
        
    
    return "sad"


if __name__ == "__main__":
    test_cases=0
    n=0
    locations=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\DFS&BFS\\input9205.txt","r") as file:
        test_cases=int(file.readline())
        for _ in range(test_cases):
            n=int(file.readline())
            locations=[]
            for _ in range(n+2):
                row,col=map(int,file.readline().split())
                locations.append((row,col))
            print(solution())