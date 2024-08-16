""""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
"""

min_value = float('inf')
    max_value = float('-inf')
    max_distance = 0
    
    for arr in arrays:
        # Current array's smallest and largest elements
        current_min = arr[0]
        current_max = arr[-1]
        
        # Calculate the distance with current array's max and global min
        if min_value != float('inf'):
            max_distance = max(max_distance, abs(current_max - min_value))
        
        # Calculate the distance with current array's min and global max
        if max_value != float('-inf'):
            max_distance = max(max_distance, abs(current_min - max_value))
        
        # Update global min and max
        min_value = min(min_value, current_min)
        max_value = max(max_value, current_max)
    
    return max_distance
