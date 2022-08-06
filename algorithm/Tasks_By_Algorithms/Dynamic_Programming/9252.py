def solution():
    str1_length=len(str1)
    str2_length=len(str2)

    di=[[0] * (str1_length+1) for _ in range(str2_length+1)]
    lcs=[]
    for i in range(1,str2_length+1):
        for j in range(1,str1_length+1):
            if str2[i-1]==str1[j-1]:
                di[i][j]=di[i-1][j-1]+1
            else:
                di[i][j]=max(di[i-1][j],di[i][j-1])
 
    row=str2_length
    col=str1_length

    lcs=""
    while di[row][col] !=0:
        if di[row-1][col]==di[row][col]:
            row-=1
        elif di[row][col-1]==di[row][col]:
            col-=1
        else:
            lcs=str1[col-1]+lcs
            row-=1
            col-=1

    print(len(lcs))
    print(lcs)

if __name__ == "__main__":
    str1,str2="",""

    with open("input9252.txt","r") as file:
        str1=list(file.readline().strip())
        str2=list(file.readline().strip())
    
    print(str1,str2)
    
    solution()