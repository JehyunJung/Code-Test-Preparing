def solution(s):
    answer = len(s)
    for term in range(1,len(s)//2 +1):
      index=0
      compressed_string=''
      while index<len(s):
        split_string=s[index:index+term]
        index+=term
        count=1
        while s[index:index+term] == split_string:
          count+=1
          index+=term
        if count>=2:
          compressed_string+=str(count)+split_string
        else:
          compressed_string+=split_string
      answer=min(answer,len(compressed_string))
        
    return answer

s=0
with open("input9.txt","r") as file:
  s=file.readline()
print(solution(s))