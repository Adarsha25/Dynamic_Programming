def min_subarray_sum(array):
    if len(array) == 0:
        return 0

    min_sum_using_element = [array[0]]
    min_sum = array[0]

    for i in range(1, len(array)):
        num = array[i]
        current_min = min(num, min_sum_using_element[i-1])
        min_sum_using_element.append(current_min)
        min_sum = min(min_sum, current_min)

    return min_sum
a = [-2, 1, 3, 4, 5, -7, -9, -10]
print(min_subarray_sum(a))
