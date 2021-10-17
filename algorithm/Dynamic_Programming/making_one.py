import sys


def one_operation(n):
    data = [0] * (n + 1)

    if data == 1:
        return 1

    data[0], data[1] = 0, 0

    for temp in range(2,n+1):
      data[temp] = data[temp - 1] + 1
      if temp % 2 == 0:
          data[temp] = min((data[temp // 2] + 1), data[temp])
      if temp % 3 == 0:
          data[temp] = min((data[temp // 3] + 1), data[temp])
      if temp % 5 == 0:
          data[temp] = min((data[temp // 5] + 1), data[temp])
    return data[n]


n = int(sys.argv[1])
print(one_operation(n))
