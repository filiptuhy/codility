int solution(int X, int Y, int D) {

    int distance = Y-X;
    
    int jumps = distance/D;
    int zvysok = distance%D;
    if(zvysok ==0){}
    else if(zvysok <D) jumps++;
 
    return jumps;
}
