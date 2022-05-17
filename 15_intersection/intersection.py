def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # turn l2 into a set 
    set2 = set(l2)
    print(set2)
    # use comprehension for value in list 1 if val is in set 2 then add it as a value to be returned
    return [val for val in l1 if val in set2]