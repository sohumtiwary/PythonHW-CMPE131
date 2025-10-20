def merge_list(list1, list2):
    if type(list1) is not list or type(list2) is not list:
        raise TypeError("Both inputs must be lists.")

    # Check to make sure all elements are integers
    if any(not isinstance(num, int) for num in list1 + list2):
        raise TypeError("All elements must be integers.")

    combined = list1 + list2
    return _merge_sort(combined)


def _merge_sort(items):
    if len(items) <= 1:
        return items.copy()

    midpoint = len(items) // 2
    left_half = _merge_sort(items[:midpoint])
    right_half = _merge_sort(items[midpoint:])
    return _merge_parts(left_half, right_half)


def _merge_parts(left, right):
    merged, i, j = [], 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged
