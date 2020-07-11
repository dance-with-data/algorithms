def merge_sort(x):
   
    # inouts:
    # x : a numpy array to be sorted 
    # outputs:
    # A : sorted (ascending) verion of x
    
    A = np.copy(x)
    
    if len(A) == 1:
        return(A)
    else:
        p = 0
        r = len(A) // 2
        if p < r:
            # create left and right arrays:
            L = merge_sort(A[p:r])
            R = merge_sort(A[r:len(A)])
            # merge L and R: index i for L array and j for R array
            i = 0
            j = 0
            for k in range(0, len(A)):
                # there are 3 cases: 1) L and R are not finished, 2) R is finished and L is not, and 3) L is finished and R is not
                if i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        A[k] = L[i]
                        i += 1
                    elif L[i] > R[j]:
                        A[k] = R[j]
                        j += 1
                        # print("1 ) i = " + str(i) + " j = " + str(j))
                elif i < len(L) and j == len(R):
                    A[k] = L[i]
                    i += 1
                    # print("2) i = " + str(i) + " j = " + str(j))
                elif (i == len(L) and j < len(R)):
                    A[k] = R[j]
                    j += 1
                    # print("3) i = " + str(i) + " j = " + str(j))
        return(A)

