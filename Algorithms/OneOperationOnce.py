def operation(A):
    A.sort()
    low = A[0]
    high = A[len(A)-1]
    mid = int((low+high)/2)
    if A[mid] = high:
        A[high] = mid
        
    return
    
operation(list(map(int, input().split())))
