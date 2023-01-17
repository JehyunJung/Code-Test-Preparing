from itertools import product
def solution():
    max_count=0
    for start_row,start_col in product(set(rows),set(cols)):
        count=0
        for row,col in zip(rows,cols):
            if start_row<=row<=start_row+t_length and start_col<=col<=start_col+t_length:
                count+=1
        max_count=max(max_count,count)
    
    return n_stars-max_count
        
        
if __name__ == "__main__":
    with open("input14658.txt","r") as file:
        n_rows,n_cols,t_length,n_stars=map(int,file.readline().split())
        rows=[]
        cols=[]

        for _ in range(n_stars):
            row,col=map(int,file.readline().split())
            rows.append(row)
            cols.append(col)
               
    print(solution())