from collections import defaultdict
def solution():
    number_counter=defaultdict(int)

    for number in numbers:
        number_counter[number]+=1

    count=0

    target_numbers=sorted(list(number_counter.keys()))
    handled=set()

    for operand1 in target_numbers:
        for operand2 in target_numbers:
            result=operand1+operand2

            #사용한 횟수만큼 count수 감소
            number_counter[operand1]-=1
            number_counter[operand2]-=1
            number_counter[result]-=1

            if number_counter[operand1] >=0 and number_counter[operand2] >=0 and number_counter[result] >=0:
                handled.add(result)
            
            #사용한 횟수만큼 count 수 증가
            number_counter[operand1]+=1
            number_counter[operand2]+=1
            number_counter[result]+=1

    print(handled)

    for target_number in target_numbers:
        if target_number in handled:
            count+=number_counter[target_number]
    
    return count

if __name__ == "__main__":
    with open("input1253.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    print(solution())