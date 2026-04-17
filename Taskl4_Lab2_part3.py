def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # words: ['this', 'is', 'confusin'm\, 'code.', 'AVOID', 'SUCH.']
         # first: ['this', 'is', confusing', 'code.', 'AVOID'] second: ['this', 'is', 'confusing', 'code', 'AVOID', 'SUCH.']
         # The lists became mutable so they are all the same with every change
print(first)
print(second)
print(words)
