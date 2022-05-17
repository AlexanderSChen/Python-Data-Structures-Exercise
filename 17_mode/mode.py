def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # make a dic to house the keys and value pairs of each number and frequency
    counts = {}
    # loop through the numbers and add 1 to the value for each time it is encountered
    for num in nums:
        # use counts.get(key num, at index 0) + 1 to the index
        counts[num] = counts.get(num, 0) + 1

    print(counts)

    # use max of count's values to get the highest count
    max_value = max(counts.values())

    # loop through the keys and values in counts items
    for (num, freq) in counts.items():
        # if the freq or value is equal to the max_value return the first number if there is more than one max number
        if freq == max_value:
            return num