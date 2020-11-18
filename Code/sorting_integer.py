#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Where k is the maximum value, because it loops over
                  a list of n size and one of k size
    Memory usage: O(k) Because it declares an array of size k
    """
    # Initialize list
    count_list = []

    # Iterate over numbers
    for num in numbers:
        # If the list isn't big enough, extend it
        if len(count_list) < num + 1:
            count_list.extend([0] * (num - len(count_list) + 1))
        # Increase the appropriate count
        count_list[num] += 1

    # Empty original list
    numbers[:] = []
    # Add v (count value) entries of i (index) to original list
    for i, v in enumerate(count_list):
        numbers.extend([i] * v)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k) where k is the number of buckets, as it loops over
                  each element and each bucket
    Memory usage: O(n+k) as it declares buckets and adds each element to them
    """
    # Initialize max value and bucket list
    max_value = max(numbers)
    buckets = [[]] * num_buckets + 1

    # Sort all numbers into appropriate buckets
    for num in numbers:
        buckets[num * len(buckets) / (max_value + 1)].append(num)

    # Clear original list
    numbers[:] = []
    # Sort each bucket and append it to the list
    for bucket in buckets:
        if len(bucket) > 0:
            counting_sort(bucket)
            numbers.extend(bucket)
