def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    sumA = sum(A)
    sumB = sum(B)
    
    diff = sumA + 10 - sumB
    
    # must be even to divide by 2
    if diff % 2 != 0:
        return None
    
    target = diff // 2  # we want a - b = target
    
    i = 0
    j = 0
    
    while i < len(A) and j < len(B):
        current = A[i] - B[j]
        
        if current == target:
            return (i, j)
        elif current < target:
            i += 1
        else:
            j += 1
    
    return None
