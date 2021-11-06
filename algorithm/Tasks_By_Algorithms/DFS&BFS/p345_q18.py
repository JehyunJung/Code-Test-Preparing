def find_balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def check_if_correct(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True

def solution(p):
    answer = ''
    
    if p=='':
        return answer
    
    index=find_balanced_index(p)
    
    u=p[:index+1]
    v=p[index+1:]
    
    if check_if_correct(u):
        answer=u+solution(v)
    else:    
        answer='('
        answer+=solution(v)
        answer+=')'

        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer+=''.join(u)
    return answer

p=0
with open("input18.txt","r") as file:
  p=file.readline()

print(solution(p))