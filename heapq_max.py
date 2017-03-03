import sif

def push_heap(A, val):
    '''Pushes a value onto the heap `A` while keeping the heap property 
    intact.  The heap size increases by 1.'''
    A.append(val)
    sif.__siftup(A, len(A) - 1)   # furthest left node
    return

def pop_heap(A):
    '''Returns the max value from the heap `A` while keeping the heap
    property intact.  The heap size decreases by 1.'''
    n = len(A) - 1
    #__swap(A, 0, n)
    A[0], A[n] = A[n], A[0]
    max = A.pop(n)
    sif.__siftdown(A, 0)
    return max
