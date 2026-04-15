def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # when a is greater than both b and c
    elif b > c:
        return b + c             # when b is greater than both a and c
    else:
        return 2 * c             # when c is greater than both a and b


answer1 = function2(3, 2, 1)     # 1
answer2 = function2(2, 3, 1)     # 4
answer3 = function2(2, 1, 3)     # 6
print(answer1)
print(answer2)
print(answer3)