def solution(A):
    B = range(1, (len(A)+2))
    a = set(A)
    b = set(B)
    result = [i for i in b if i not in a]
    return result[0]
---------------------
class Solution {
    public int solution(int[] A) {
        int araySum = 0;
        int fullSum = 0;
        for(int i = 0;i<A.length;i++)
        {
         araySum += A[i];
         fullSum += i; 
        }
        fullSum += A.length;
        fullSum += A.length+1;
        return fullSum - araySum;
    }
}
