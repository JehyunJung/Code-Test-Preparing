from collections import Counter

def extract_cols(n_rows,n_cols,rows):
    cols=[]
    for col_index in range(n_cols):
        col=[]
        for row_index in range(n_rows):
            col.append(rows[row_index][col_index])
        cols.append(col)
    
    return cols

def extract_rows(n_rows,n_cols,cols):
    rows=[]
    for row_index in range(n_rows):
        row=[]
        for col_index in range(n_cols):
            row.append(cols[col_index][row_index])
        rows.append(row)
    
    return rows

def operation_R(rows,n_rows):
    largest_size=0
    for row_index in range(n_rows):
        temp_row=[]
        row_Counter=list(Counter(rows[row_index]).items())
        row_Counter.sort(key=lambda x : (x[1],x[0]))
        for key,value in row_Counter:
            if key==0:
                continue
            temp_row.append(key)
            temp_row.append(value)

        rows[row_index]=temp_row
        largest_size=max(largest_size,len(temp_row))
    
    largest_size=min(largest_size,100)
    #append 0 for blank spots
    for row_index in range(n_rows):
        row_size=len(rows[row_index])

        if row_size >= 100:
            rows[row_index]=rows[row_index][:101]
            continue

        rows[row_index].extend([0]*(largest_size-row_size))
    
    #열 늘려주기
    return largest_size

def operation_C(cols,n_cols):
    largest_size=0
    for col_index in range(n_cols):
        temp_col=[]
        col_Counter=list(Counter(cols[col_index]).items())
        col_Counter.sort(key=lambda x : (x[1],x[0]))
        for key,value in col_Counter:
            if key==0:
                continue
            temp_col.append(key)
            temp_col.append(value)
        cols[col_index]=temp_col
        largest_size=max(largest_size,len(temp_col))
    
    largest_size=min(largest_size,100)
    #append 0 for blank spots
    for col_index in range(n_cols):
        col_size=len(cols[col_index])

        if col_size >= 100:
            cols[col_index]=cols[col_index][:101]
            continue
        cols[col_index].extend([0]*(largest_size-col_size))
    
    #열 늘려주기
    return largest_size

def print_graph(times,rows):
    print("GRAPH ",times)
    for row in rows:
        print(row)

def solution():
    n_rows,n_cols=3,3
    times=0
    rows=graph
    cols=extract_cols(n_rows,n_cols,graph)

    while True:
        if times >100:
            times=-1
            break

        if r <= n_rows and c <= n_cols:
            if rows[r-1][c-1] ==k:
                break

        if n_rows >=n_cols:
            n_cols=operation_R(rows,n_rows)
            cols=extract_cols(n_rows,n_cols,rows)
        else:
            n_rows=operation_C(cols,n_cols)
            rows=extract_rows(n_rows,n_cols,cols)
        
        times+=1


    return times

if __name__ =="__main__":
    r,c,k=0,0,0
    graph=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\Implementation\\input17140.txt","r") as file:
        r,c,k=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(3)]

    print(solution())