##Algorithm:
##1. Input Q
##2. loop: While Q->0
##    2.1 Input N and loop while N-->0
##        2.1.1 Input N values in an array A.
##        2.1.2 Sort A
##        2.1.3 C = A[0]
##        2.1.4 Input K 
##        2.1.5 loop : C to length(A)
##            2.1.5.1 print A[K]
##            2.1.5.2 break loop

Q = int(input())
for i in range(0,Q):
    N = int(input())
    for j in range(0,N):
        A = list(map(int, input().split()))
        A.sort()
        c = A[0]
        l=0
        K = int(input())
        while(l!=K):
            c+=1
            l+=1
        print(c)
        break
