def check(n:int) -> bool:
    return n > 2                             # n=0=false, n=1=false, n=2=false, n=3=True, n=4=True



answer = [x for x in range(5) if check(x)]   # 3 and 4, the numbers greater than 2
print(answer)