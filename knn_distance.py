import random

def knn_distance(arr, q, k):
    
    pairs = [(x, abs(x - q)) for x in arr]

    def partition(left, right, pivot_idx):
        pivot_dist = pairs[pivot_idx][1]
        pairs[pivot_idx], pairs[right] = pairs[right], pairs[pivot_idx]

        store = left
        for i in range(left, right):
            if pairs[i][1] < pivot_dist:
                pairs[store], pairs[i] = pairs[i], pairs[store]
                store += 1

        pairs[store], pairs[right] = pairs[right], pairs[store]
        return store

    def quickselect(left, right, k_smallest):
        if left == right:
            return pairs[left]

        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)

        if k_smallest == pivot_idx:
            return pairs[k_smallest]
        elif k_smallest < pivot_idx:
            return quickselect(left, pivot_idx - 1, k_smallest)
        else:
            return quickselect(pivot_idx + 1, right, k_smallest)

    result = quickselect(0, len(pairs) - 1, k - 1)

    return (result[1], result[0])
