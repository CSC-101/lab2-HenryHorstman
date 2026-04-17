from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # on first test = False, on second test = True
    if test:                            # This prevents calling a value that is not in the list
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # The value is none
second = checked_access([1, 0, 1], 2)    # The valuer is 1
print(first)
print (second)
