def solution():
    left,right,zero=0,0,1
    row_sum=left+right+zero
    for i in range(1,num+1):
        left,right,zero=row_sum-right,row_sum-left,row_sum
        row_sum=(left+right+zero) % 9901

    return row_sum


if __name__ == "__main__":
    num=0

    with open("input1309.txt","r") as file:
        num=int(file.readline())
    
    print(solution())