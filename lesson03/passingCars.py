def solution(A):
    jednotky = 0
    auta = 0;
    for i in reversed(A):
        if auta >= 1000000000:
            return -1
        if i == 1:
            jednotky +=1
        if i == 0 and jednotky > 0:
            auta += jednotky
    return auta