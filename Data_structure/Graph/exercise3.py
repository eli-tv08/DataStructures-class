def sort1(A):
    B = [0] *len(A)
    for i in range(len(A)):
        min_value = A[0]
        k = 0
        for j in range(1 , len(A)):
            if A[j] < min_value:
                min_value = A[j]
                k = j
        B[i] = min_value
        A[k] = float("inf")
    return B 
