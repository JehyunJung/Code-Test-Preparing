from heapq import heappush,heappop

if __name__ == "__main__":
    n=int(input())
    min_number,max_number=4001,-4001
    sum_of_numbers=0
    
    count=[0]*(8001)
    max_count=0
    first_value,second_value=-4001,-4001
    
    max_heap=[]
    min_heap=[]
    for i in range(n):
        number=int(input())

        min_number=min(min_number,number)
        max_number=max(max_number,number)
        sum_of_numbers+=number
        count[number]+=1

        if count[number]==max_count:
            if first_value < number:
                if number <=second_value or second_value == -4001:
                    second_value=number

            elif number <= first_value:
                second_value=first_value
                first_value=number

        if count[number] > max_count:
            max_count=count[number]

            first_value=number
            second_value=-4001
        
        if i % 2==0:
            heappush(max_heap,(-number,number))
        else:
            heappush(min_heap,(number,number))
        
        if min_heap and max_heap[0][1] > min_heap[0][1]:
            left_value=heappop(max_heap)[1]
            right_value=heappop(min_heap)[1]

            heappush(max_heap,(-right_value,right_value))
            heappush(min_heap,(left_value,left_value))
            
    print(round(sum_of_numbers/n))
    print(max_heap[0][1])
    print(second_value if second_value != -4001 else first_value)
    print(max_number-min_number)

