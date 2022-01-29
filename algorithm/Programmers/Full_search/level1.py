def solution(answers):
    answer = []
    students=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    scores=[]
    
    for student in students:
        length=len(student)
        answer_count=0
        for question_index in range(len(answers)):
            if answers[question_index] == student[question_index%length]:
                answer_count+=1
        scores.append(answer_count)
        
    print(scores)    
    for index,score in enumerate(scores):
        if score==max(scores):
            answer.append(index+1)

    return answer

if __name__ == "__main__":
  answers=[]
  with open("level1.txt","r")as file:
    answers=list(map(int,file.readline().split()))
  print(solution(answers))