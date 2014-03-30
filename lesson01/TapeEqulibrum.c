int solution(int A[], int N) {
    int B[N];
    int i;

    if(sizeof(A)==2)
    {
        return abs(A[0]-A[1]);
    }
    B[0] = A[0];
    
    for(i=1;i<N;i++)
    {
        B[i] = B[i-1] +A[i];
    }
    
    int dif = 100000;

    for(i=0;i<N-1;i++)
    {
        if(dif>abs(B[i]-(B[N-1]-B[i])))
        {
            dif=abs(B[i]-(B[N-1]-B[i]));
        }
    } 
    return dif;
}
