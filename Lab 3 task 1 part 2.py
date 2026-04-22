def square(n:int) -> int:
    return n * n                           # n=1*1=1, n=2*2=4, n=3*3=9, n=4*4=16


squares = [square(x) for x in [1,2,3,4]]   # the value of squares = [1, 4, 9, 16] it is the square of the list provided
print(squares)                                    