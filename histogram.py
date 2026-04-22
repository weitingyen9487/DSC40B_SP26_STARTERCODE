def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    result = []
    
    i = 0  
    
    for (a, b) in bins:
        count = 0
        
        # count points in current bin [a, b)
        while i < n and points[i] < b:
            if points[i] >= a:
                count += 1
            i += 1
        
        width = b - a
        density = count / (n * width)
        result.append(density)
    
    return result
