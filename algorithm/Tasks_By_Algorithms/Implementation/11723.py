def solution():
    all_bit=2**20-1

    set_bit=0

    for operation in operations:
        if operation[0]=="all":
            set_bit=all_bit
        elif operation[0]=="empty":
            set_bit=0
        else:
            number_bit=1<<(int(operation[1])-1)
            if operation[0] =="add":
                if set_bit & number_bit == number_bit:
                    continue
                else:
                    set_bit |= number_bit
            elif operation[0] =="remove":
                if set_bit & number_bit == number_bit:
                    set_bit ^= number_bit
                else:
                    continue 
            elif operation[0]=="check":
                if set_bit & number_bit == number_bit:
                    print(1)
                else:
                    print(0)
            elif operation[0] == "toggle":
                set_bit ^= number_bit


if __name__ == "__main__":
    with open("input11723.txt","r") as file:
        n=int(file.readline())
        operations=[list(map(str,file.readline().strip().split())) for _ in range(n)]
    
    solution()


        
                         
                         
                       