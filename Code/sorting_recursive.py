#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) Passes over each element once
    Memory usage: O(n) Makes a new list for all the elements
    """
    ind_1, ind_2 = 0, 0
    new_list = []
    # Repeat until one list is empty
    while ind_1 <= len(items1) - 1 and ind_2 <= len(items2) - 1:
        # Find minimum item in both lists and append it to new list
        if items1[ind_1] <= items2[ind_2]:
            new_list.append(items1[ind_1])
            ind_1 += 1
        else:
            new_list.append(items2[ind_2])
            ind_2 += 1
    # Append remaining items in non-empty list to new list
    if ind_1 <= len(items1) - 1:
        new_list.extend(items1[ind_1:])
    elif ind_2 <= len(items2) - 1:
        new_list.extend(items2[ind_2:])
    return new_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    """
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log(n)) Passes over each element log(n) times
    Memory usage: O(n) It creates a new list to hold all the elements
    """
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # Split items list into approximately equal halves
    left = items[:len(items) // 2]
    right = items[len(items) // 2:]

    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    items[:] = merge(merge_sort(left), merge_sort(right))
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (The middle item) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    """
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[high]

    i = low
    j = high - 1

    while i < j:
        if items[j] >= pivot:
            j -= 1
        if items[i] >= pivot and items[j] < pivot:
            items[i], items[j] = items[j], items[i]
            j -= 1
            i += 1
        if items[i] < pivot:
            i += 1

    if items[i] < pivot:
        i += 1
    items[i], items[high] = items[high], items[i]
    return i


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    """
    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    print("Low", low, "High", high)
    if len(items[low:high + 1]) == 1:
        return items
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        p = partition(items, low, high)
        print("p", p)

        # Sort each sublist range by recursively calling quick sort
        print(items)
        print("Sorting low")
        quick_sort(items, low, p - 1)
        print("Sorting high")
        quick_sort(items, p + 1, high)
        print("Returning", items[low:high + 1])
