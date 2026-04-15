def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For the variable "first
    else:
        return m

first = smallest(3, 2)       # 2
second = smallest(2, 2)      # 2 yes it is reasonable because 2 is not greater than 3
print(first)
print(second)
