def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    #if list exists as a list
    if lst:
        #return the -1 index which is the last index of the list
        return lst[-1]