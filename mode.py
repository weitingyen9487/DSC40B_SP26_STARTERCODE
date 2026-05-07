def mode(numbers):
    counts = {}
    best_num = None
    best_count = 0

    for num in numbers:
        if num not in counts:
            counts[num] = 0

        counts[num] += 1

        if counts[num] > best_count:
            best_count = counts[num]
            best_num = num

    return best_num
