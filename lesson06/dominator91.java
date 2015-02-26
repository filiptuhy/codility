// you can also use imports, for example:
 import java.util.*;

// wrong for extreme_empty_and_single_item empty and single element arrays

class Solution {
    public int solution(int[] A) {
       int half = (A.length/2);
       Map<Integer,Integer> map = new HashMap<Integer,Integer>();
       for(int i = 0;i<A.length;i++)
       {
            if(!map.containsKey(A[i]))
            {
                map.put(A[i],1);
            }else
            {
                int thisOne = map.get(A[i]);
                thisOne++;
                if(thisOne > half) return i;
                map.remove(A[i]);
                map.put(A[i],thisOne);
            }
        }
        
        return -1;
    }
}
