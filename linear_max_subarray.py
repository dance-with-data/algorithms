def linear_max_subarray(x):
    
    # this function implements an algorithm with linear complexity to find a subarray that has maximum sum.
    # previously I had implemented a divide and conquer based solution of this problem and its complexity 
    # scaled as n * log(n) 
    
    # input:
    # x: a numpy array that subarray needs to be found within
    # output:
    # A tuple with 3 elements: start and end indices of the maximum subarray, sum of the elements of the maximum array
    
    A = np.copy(x)
    
    # begin and end indices of the maximum subarray in the input array
    head = []
    tail = []
    
    # sum of the all the elements of the maximum subarray
    S_max = float("-inf")
    
    # partial sum from the beginning of the best subarray till current element
    S_par = 0
        
    # new head for the new best subarray
    new_head = 0
    
    for i in range(0, len(A)): 
        
        S_par = S_par + A[i]
        
        if S_par > S_max:
            S_max = S_par
            tail = i
            head = new_head
        if S_par < 0:
            S_par = 0
            new_head = i +1
    
    return((head, tail, S_max))