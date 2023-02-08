def solution():
    for gender, number in students:
        #남학생인 경우
        if gender ==1:
            for index in range(number,n+1,number):
                switches[index-1]=1-switches[index-1]
        
        #여학생인 경우
        else:
            middle_index=number-1
            print(middle_index)
            #가장 큰 최대 구간 찾기
            for size in range(n//2):
                print(middle_index-size,middle_index+size)
                #범위를 넘어서는 경우
                if middle_index-size < 0 or middle_index+size >=n:
                    break     
                #size에 대한 구간에 스위치가 좌우대칭 상태가 아닌 경우에는 넘어간다.
                if switches[middle_index-size] != switches[middle_index+size]:
                    break
                              
                switches[middle_index-size]=1-switches[middle_index-size]
                switches[middle_index+size]=1-switches[middle_index+size]
        print(*switches)
    
    for index in range(1,n+1):
        print(switches[index-1],end=" ")
        if index % 20==0:
            print()

if __name__ == "__main__":
    with open("input1244.txt","r") as file:
        n=int(file.readline())
        switches=list(map(int,file.readline().split()))
        n_students=int(file.readline())
        students=[list(map(int,file.readline().split())) for _ in range(n_students)]
    solution()