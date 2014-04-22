'''
Reservoir Sampling

'''

import random 

def random_subset( iterator, K ): 
    result = [] 
    counter = 0 
    for item in iterator: 
        counter += 1 
        if len( result ) < K: 
            result.append( item ) 
        else: 
            s = int(random.random() * counter) 
            if s < K: 
                result[ s ] = item 
    return result