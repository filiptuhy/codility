def solution(A):
    B = range(1, (len(A)+2))
    a = set(A)
    b = set(B)
    result = [i for i in b if i not in a]
    return result[0]
