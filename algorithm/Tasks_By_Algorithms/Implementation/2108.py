from collections import Counter
def solution():

    numbers.sort()
    number_counter=Counter(numbers).most_common()
    max_count=number_counter[0][1]

    mode=number_counter[0][0]

    if n >1 and number_counter[1][1] == max_count:
        mode=number_counter[1][0]

    print(round(sum(numbers)/n))
    print(numbers[n//2])
    print(mode)
    print(max(numbers)-min(numbers))

if __name__ == "__main__":
    with open("input2108.txt","r") as file:
        n=int(file.readline())
        numbers=[int(file.readline()) for _ in range(n)]
    solution()