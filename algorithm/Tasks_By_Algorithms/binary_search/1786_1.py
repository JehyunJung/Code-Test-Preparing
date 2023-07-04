def solution(P,S):
   ans=[]  
   if S in P:
     return ans   
      
      
if __name__ == "__main__":
   P,S="",""
   with open("input1786.txt","r") as file:
      P=file.readline()
      S=file.readline()

   result=solution(P,S)
   print(len(result))
   print(*result)