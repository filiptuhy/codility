def solution(A):
    B = range(1, (len(A)+1))
    a = set(A)
    b = set(B)
    result = [i for i in b if i not in a]
    if not result:
        return 1
    else:
        return 0
