import random

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len (array) > 1:

        pivot = random.choice(array)

        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        return quicksort(less)+ equal + quicksort(greater)
    
    else: 
        return array

