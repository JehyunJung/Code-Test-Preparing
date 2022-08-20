def rotation(dir):
    if dir == 3:
        return 0

    return dir+1

def dragon_curve_maker():
    dragon_curves=dict()
    dragon_curves[0]=[[0]]
    dragon_curves[1]=[[1]]
    dragon_curves[2]=[[2]]
    dragon_curves[3]=[[3]]

    for generation in range(10):
        for type in range(4):
            past_dragon_curve=dragon_curves[type][generation]
            dragon_curves[type].append(past_dragon_curve+list(map(rotation,past_dragon_curve[::-1])))

    return dragon_curves

def print_graph(graph):
    for i in range(101):
        print(graph[i])

def solution():
    graph=[[False] * 101 for _ in range(101)]

    dy=[0,-1,0,1]
    dx=[1,0,-1,0]

    dragon_curves=dragon_curve_maker()

    for start_col,start_row,type,generation in curves:
        row,col=start_row,start_col
        graph[start_row][start_col]=True
        for dragon_curve_direction in dragon_curves[type][generation]:
            col+= dx[dragon_curve_direction]
            row+= dy[dragon_curve_direction]
            graph[row][col]=True

    count=0
    for row in range(101):
        for col in range(101):
            if graph[row][col] == True and graph[row+1][col] == True and graph[row][col+1] == True and graph[row+1][col+1] == True:
                count+=1
    
    return count





if __name__ == "__main__":
    num=0
    curves=[]

    with open("input15685.txt","r") as file:
        num=int(file.readline())

        curves=[list(map(int,file.readline().split())) for _ in range(num)]
    
    print(solution())