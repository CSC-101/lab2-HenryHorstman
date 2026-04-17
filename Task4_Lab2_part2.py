def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # The first variable
    elif len(L) > 1:                                  #   "4", "2", and "2" = 9
        result = len(L[0]) + len(L[1])                # The third variable
    elif len(L) > 0:                                  #   "7" + "4" = 11
        result = len(L[0])                            # The second variable
    else:                                             # "11"
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first)
print(second)
print(third)