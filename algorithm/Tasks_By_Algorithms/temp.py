from functools import reduce
def test(*number):
    print(number)
    temp = reduce(lambda x, y: x * y, number)
    print(temp)

test(*[1,2,3,4,5])