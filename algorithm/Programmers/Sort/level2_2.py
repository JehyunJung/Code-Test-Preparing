def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(citations[-1]):
        count=0
        for citation in citations:
            if citation >= i:
                count+=1
        if count >= i:
            answer=max(answer,i)
               
            
    return answer

if __name__== "__main__":
  citations=[]
  with open("level3.txt","r") as file:
    citations=list(map(int,file.readline().split()))
  print(solution(citations))