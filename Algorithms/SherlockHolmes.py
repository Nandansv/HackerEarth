#Algorithm as follows.





T = int(input())
c = 0
for i in range(0,T):
    N,K,P = map(int, input().split())
    A = list(map(int, input().split()))
    for k in range(0,len(A)):
        if(A[k] <= P+c):
            c+=1
    if(K+P <=N):
        print(P+c)
        c=0
    else:
        print("-1")
        c=0
    
        
            









    
        

    

    
    
