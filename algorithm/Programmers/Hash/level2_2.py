def solution(clothes):
    answer = 0
    clothes_dictionary={}
    
    for cloth,clothe_type in clothes:
        if clothe_type in clothes_dictionary.keys():
            clothes_dictionary[clothe_type]+=1
        else:
            clothes_dictionary[clothe_type]=1
    
    answer=1
    for count in clothes_dictionary.values():
        answer *= (count+1)
    answer-=1
    
    return answer

if __name__ == "__main__":
  n=0
  clothes=[]

  with open("level2_2.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      clothe,clothe_type=map(str,file.readline().split())
      clothes.append((clothe,clothe_type))
  print(solution(clothes))