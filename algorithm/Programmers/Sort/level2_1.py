def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    temp_array=[(number*(12//len(number)),number) for number in numbers]
    temp_array.sort(reverse=True)
    for key,number in temp_array:
        answer+=number
    return str(int(answer))

if __name__ == "__main__":
  numbers=[]
  with open("level2_1.txt","r") as file:
    numbers=list(map(int,file.readline().split()))
  print(solution(numbers))