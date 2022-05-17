def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
    # old = 0
    # oldest = 0
    # for age in ages:
    #     if age > oldest:
    #         old = oldest
    #         oldest = age

    # return (old, oldest)

    # create a set for ages so it can be sorted with index stepper and it eliminates multiples of the same value
    uniq_ages = set(ages)
    print(uniq_ages)
    # start at -2 index which means it starts at the second to last item in the list and since the list is sorted the highest values are at the end 
    oldest = sorted(uniq_ages)[-2:]
    print(oldest)
    # return the oldest values as tuples
    return tuple(oldest)


    # uniq_ages = set(ages)
    # oldest = None
    # second = None

    # loop through the unique ages
    # for age in uniq_ages:
        # if oldest is none or if age is greater than oldest
        # if oldest is None or age > oldest:
            # set second to be oldest, which is the older, smaller value
            # second = oldest
            # set oldest to be age which is the new oldest value
            # oldest = age
        #if second is None or age is greater than second then set second = to age 
    #     elif second is None or age > second:
    #         second = age
    # return (second, oldest)