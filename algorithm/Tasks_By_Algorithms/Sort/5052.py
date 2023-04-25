import sys
def solution(n,phonenumbers):
    phonenumbers.sort()
    
    for i in range(1,n):
        if phonenumbers[i].startswith(phonenumbers[i-1]):
            print("NO")
            return
    print("YES")
     

if __name__ == "__main__":
    sys.stdin=open("input5052.txt", "r")
    n_testcases=int(input())

    for _ in range(n_testcases):
        n_numbers=int(input())
        solution(n_numbers,[input() for _ in range(n_numbers)])