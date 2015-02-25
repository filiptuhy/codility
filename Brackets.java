class Solution {
    public int solution(String S) {
        int parenth = 0;
        Stack stack = new Stack();
        for( char c : S.toCharArray()) 
        {
            switch (c)
            {
                case '{': {stack.push('{');  break;}
                case '(': {stack.push('('); break;}
                case '[': {stack.push('['); break;}
                case '}': 
                    {
                          if(stack.empty()) return 0;
                          if(stack.peek().equals('{')) { stack.pop(); break;}
                            else return 0;
                    }
                case ')': 
                    {
                          if(stack.empty()) return 0;
                          if(stack.peek().equals('(')) { stack.pop(); break;}
                            else return 0;
                    }
                case ']': 
                    {
                          if(stack.empty()) return 0; 
                          if(stack.peek().equals('[')) { stack.pop(); break;}
                            else return 0;
                    }
                            
                }
        }
        if(stack.empty())
            return 1;
        return 0;
    }
}
