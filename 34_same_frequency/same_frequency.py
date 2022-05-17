def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))

def freq_counter(coll):
    # create a dictionary to hold the counts of each number
    counts = {}

    # loop through  collection of numbers
    for x in coll:
        # add one to the value of x key for each number encountered which creates the key and iterates the value for each encounter of the number key using .get of x index 0 
        counts[x] = counts.get(x, 0) + 1
    
    return counts