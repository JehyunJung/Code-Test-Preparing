def solution(phone_book):
  length=len(phone_book)
  phone_book_sorted_by_value=sorted(phone_book)

  for target_index in range(length-1):
      if phone_book_sorted_by_value[target_index+1].startswith(phone_book_sorted_by_value[target_index]):
          return False
  return True

if __name__=="__main__":
  phone_book=[]

  with open("level2_1.txt","r") as file:
    phone_book=list(map(str,file.readline().split()))
  
  print(solution(phone_book))