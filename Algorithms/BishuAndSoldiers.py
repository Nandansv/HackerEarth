#function to search and compare
def CompareNcount(A,K):
        if(K>=len(A)):
                cnt = len(A)-1
        else:
                cnt = A.index(K)
        k = 0
        for i in range(0,cnt+1):
                k +=A[i]
        print(cnt+1,k)
        return
                
##        count = 0
##        Sum = 0
##        #assign the key value to the max iterative value.
##        for i in range(0,len(A)):
##                if(A[i]<=K):
##                        count+=1
##                        Sum = Sum + A[i]
##        print(count,Sum)
##        return

#Take inputs of N,A,Q,K from user
N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for j in range(0,Q):
        K = int(input())
        CompareNcount(A,K)
        
        

