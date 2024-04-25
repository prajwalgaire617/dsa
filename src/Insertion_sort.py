import time
def insertion_sort(A):

    start_time=time.time()
    for i in range(1,len(A)):
        key = A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j-=1
        
        A[j+1]=key
    end_time=(time.time()-start_time)*1000
    return [A,end_time]
