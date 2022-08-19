from math import ceil
def solution():
    count=num
    for student in array:
        if student-main>0:
            count+=ceil((student-main)/sub)
    
    return count

if __name__ == "__main__":
    num=0
    array=[]
    main,sub=0,0

    with open("input13458.txt","r") as file:
        num=int(file.readline())
        array=list(map(int,file.readline().split()))
        main,sub=map(int,file.readline().split())
    
    print(solution())