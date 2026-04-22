def inc(m:int) -> int:
    return m + 1                             # m=3+1=4, m=4+1=5



def check(n:int) -> bool:
    return n > 2                             # n=0=False, n=1=False, n=2=False n=3=True, n=4=True



answer = [inc(x) for x in range(5) if check(x)]   # [4, 5]
print(answer)