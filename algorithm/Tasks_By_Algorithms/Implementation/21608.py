from tracemalloc import StatisticDiff


def calculate_satisfaction():
    sum_satisfaction=0

    for row in range(num):
        for col in range(num):
            student_number=graph[row][col]
            satisfaction=0
            for dir in range(4):
                new_row=row+dy[dir]
                new_col=col+dx[dir]

                if new_row < 0 or new_row>=num or new_col < 0 or new_col>=num:
                    continue
                
                if graph[new_row][new_col] in favorites[student_number]:
                    satisfaction+=1

            #주위에 좋아하는 학생이 없으면 만족도는 0
            if satisfaction ==0 :
                sum_satisfaction+=0
            else:
                sum_satisfaction+=(10**(satisfaction-1))
    return sum_satisfaction
                
        
def solution():
    for student in student_order:
        best_row,best_col=0,0
        favorite_space_candidates=[[] for _ in range(5)] #후보칸
        #인접한 칸의 좋아하는 학생 수
        for row in range(num):
            for col in range(num):

                #빈자리가 아닌 경우 넘어간다.
                if graph[row][col] !=0:
                    continue

                favorite_count=0
        
                for dir in range(4):
                    new_row=row+dy[dir]
                    new_col=col+dx[dir]

                    if new_row < 0 or new_row>=num or new_col < 0 or new_col>=num:
                        continue
                    
                    if graph[new_row][new_col] in favorites[student]:
                        favorite_count+=1
                #인접하는 칸에 있는 좋아하는 학생의 수를 조사해서, 좋아하는 학생 수에 대한 행/열 리스트를 만든다.
                favorite_space_candidates[favorite_count].append((row,col))

        #좋아하는 학생 수가 가장 많은 칸이 여러 개가 될때, 해당 칸 들에 대한 인접한 빈칸을 조사해야한다.
        blank_space_candidates=[[] for _ in range(5)]

        #인접한 칸의 빈 칸 확인
        for i in range(4,-1,-1):
            #인접한 칸에 대해 좋아하는 학생 수가 i 인 칸이 없는 경우 검사를 생략한다.
            if len(favorite_space_candidates[i])==0:
                continue
            #만약 인접한 칸에 좋아하는 학생의 수가 가장 많은 칸이 1칸이면 해당 칸에 학생을 배치한다.
            elif len(favorite_space_candidates[i])==1:
                (best_row,best_col)=favorite_space_candidates[i][0]
                break
            
            for row,col in favorite_space_candidates[i]:
                blank_count=0
                for dir in range(4):
                    new_row=row+dy[dir]
                    new_col=col+dx[dir]

                    if new_row < 0 or new_row>=num or new_col < 0 or new_col>=num:
                        continue
                    #인접한 칸에 빈칸의 개수를 조사한다.
                    if graph[new_row][new_col]==0:
                        blank_count+=1

                blank_space_candidates[blank_count].append((row,col))
            break
        #여기까지도 자리가 설정이 안되는 경우 행/열이 가장 작은 자리 반환
        for i in range(4,-1,-1):
            #인접한 칸에 대해 빈칸의 수가 i 인 칸이 없는 경우 검사를 생략한다.
            if len(blank_space_candidates[i])==0:
                continue
            #만약 가장 많은 인접한 빈칸을 가진 칸이 한 개 인 경우 해당 칸에 학생을 배치한다.
            elif len(blank_space_candidates[i])==1:
                (best_row,best_col)=blank_space_candidates[i][0]
                break

            #인접한 칸에 좋아하는 학생 수가 가장 많은 칸 - > 인접한 빈 칸이 많은 칸 -> 행/열 이 최소가 되는 칸
            blank_space_candidates[i].sort(key=lambda x: (x[0],x[1]))
            (best_row,best_col)=blank_space_candidates[i][0]
            break

        #최종적으로 조건에 부합하는 칸에 학생 배치
        graph[best_row][best_col]=student
    
    #학생들의 총 만족도를 조사한다.
    return calculate_satisfaction()

    
    
if __name__ == "__main__":
    num=0
    favorites=[]
    graph=[]
    student_order=[]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    with open("input21608.txt","r") as file:
        num=int(file.readline())
        graph=[[0] * num for _ in range(num)]
        favorites=[[] for _ in range(num**2 +1)]
        for _ in range(num**2):
            student_num,s1,s2,s3,s4=map(int,file.readline().split())
            student_order.append(student_num)
            favorites[student_num]=[s1,s2,s3,s4]

    print(solution())