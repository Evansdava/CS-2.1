#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because it can loop through all items in the list
    Memory usage: O(1) Only declares a single counter variable
    """
    # First item doesn't need to be checked
    i = 1
    # Loop through all items
    while i < len(items):
        # If any are out of order, return False
        if items[i] < items[i - 1]:
            return False
        i += 1
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n**2) because it passes through n/2 (on average) elements
        n-1 times, which simplifies to n elements n times, n**2
    Memory usage: O(1), as only a boolean and two integers are declared
    """

    # Take up to n-1 passes
    for j in range(len(items) - 1):
        # Bool for checking if items were swapped
        swapped = False

        # Last item after each pass is always sorted and can be ignored
        for i in range(len(items) - 1 - j):

            # Swap items if the current is greater than the next
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True

        # If there were no swaps, list is already sorted
        if not swapped:
            return items
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n**2) As it loops through the whole array for each element
    Memory usage: O(1) Sorting is done in place on the array
    """
    # Loop through each index
    for i in range(len(items)):
        # Find the smallest unsorted value
        ind = items.index(min(items[i:]), i)
        # Switch it with the current index
        items[ind], items[i] = items[i], items[ind]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n**2) It can iterate through all elements on each loop
    Memory usage: O(1) Sorting is done in place, only ints declared
    """
    # Loop through the whole array
    for i in range(1, len(items)):
        # While the element is less than the element before it, swap them
        # Stop swapping if there are no elements before it
        j = i
        while items[j] < items[j - 1] and j > 0:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items
