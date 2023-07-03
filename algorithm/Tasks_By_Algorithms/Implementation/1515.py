import sys

def solution():
    #자리수를 체크하기 위한 변수 1,10,100의 자리
    current_digits=[0,0,0]

    length=len(number_string)
    for index in range(length):
        number=number_string[index]

        #현재 탐색하고 있는 일의 자리보다 작은 숫자가 들어오면 십의 자리수를 1만큼 증가시킨다.
        if number <= current_digits[0]:
            
            #만일 탐색된 숫자의 값이 기존의 십의 자리, 백의자리와 겹치면 십의 자리를 늘리지 않고, 일의자리 값만 1만큼 증가시킨다.
            if number !=0 and number in current_digits[1:]:
                current_digits[0]+=1
                continue
            current_digits[1]+=1

            #백의 자리 넘겨주기
            if current_digits[1] ==10:
                current_digits[2]+=1
                current_digits[1]=0

            current_digits[0]=0

        else:
            current_digits[0]=number

    predicted_number=current_digits[1] * 10 + current_digits[2] * 100


    #백의 자리수 혹은 십의 자리수와 같지 않은 경우, 일의 자리 값을 추가해준다.
    if number_string[length-1] not in current_digits[1:]:
        predicted_number+=current_digits[0]

    print(current_digits,predicted_number)       


if __name__ == "__main__":
    sys.stdin=open("input1515.txt","r")
    number_string=list(map(int,input()))

    solution()