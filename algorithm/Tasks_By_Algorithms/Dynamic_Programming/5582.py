def print_list(list):
    print("DI")
    for row in list:
        print(row)
def solution():
    str1_length=len(str1)
    str2_length=len(str2)

    di=[[0] * (str1_length+1) for _ in range(str2_length+1)]
    max_count=0
    for i in range(1,str2_length+1):
        for j in range(1,str1_length+1):
            if str2[i-1]==str1[j-1]:
                di[i][j]=di[i-1][j-1] + 1
                max_count=max(max_count,di[i][j])
    
    return max_count


if __name__ == "__main__":
    str1,str2="",""

    with open("input5582.txt","r") as file:
        str1=list(file.readline().strip())
        str2=list(file.readline().strip())

    print(solution())