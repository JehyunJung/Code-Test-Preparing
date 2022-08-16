def rotate_dice(dir,dice_row,dice_col):
    if dir==1:
        #동쪽
        dice_row.insert(0,dice_col.pop(-1))
        dice_col.append(dice_row.pop(-1))
        dice_col[1]=dice_row[1]
    elif dir==2:
        #서쪽
        dice_row.append(dice_col.pop(-1))
        dice_col.append(dice_row.pop(0))
        dice_col[1]=dice_row[1]
    elif dir==3:
        #북쪽
        dice_col.append(dice_col.pop(0))
        dice_row[1]=dice_col[1]
    
    elif dir==4:
        #남쪽
        dice_col.insert(0,dice_col.pop(-1))
        dice_row[1]=dice_col[1]

    
def solution():
    dice_row=[0,0,0]
    dice_col=[0,0,0,0]

    dy=[0,0,-1,1]
    dx=[1,-1,0,0]

    row,col=start_row,start_col
    
    for operation in operations:
        next_row=row+dy[operation-1]
        next_col=col+dx[operation-1]

        if next_row < 0 or next_row >= n_rows or next_col < 0 or next_col >=n_cols:
            continue

        rotate_dice(operation,dice_row,dice_col)

        if graph[next_row][next_col]==0:
            graph[next_row][next_col]=dice_col[3]

        else:
            dice_col[3]=graph[next_row][next_col]
            graph[next_row][next_col]=0
        
        row=next_row
        col=next_col

        print(dice_col[1])
    
    

if __name__ == "__main__":
    n_rows,n_cols,start_row,start_col,n_operations=0,0,0,0,0
    graph=[]
    operations=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input14499.txt","r") as file:
        n_rows,n_cols,start_row,start_col,n_operations=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]
        operations=list(map(int,file.readline().split()))
    
    solution()