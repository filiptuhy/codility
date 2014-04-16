def solution(A):
    A.sort()
    max01 = A[len(A)-1]
    max02 = A[len(A)-2]
    max03 = A[len(A)-3]
    maxRes = max01*max02*max03
    min01 = A[0]
    min02 = A[1]
    minS = min01*min02
    if minS >0:
        if minS*max01 > maxRes:
            maxRes =minS*max01
        if minS*max02 > maxRes:
            maxRes =minS*max02
        if minS*max03 > maxRes:
            maxRes =minS*max03        
    return maxRes
        