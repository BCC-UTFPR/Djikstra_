def __siftdown(A, node):
    '''Traverse down a binary tree `A` starting at node `node` and 
    turn it into a max-heap'''
    child = 2*node + 1
    # base case, stop recursing when we hit the end of the heap
    if child > len(A) - 1:
        return
    # check that second child exists; if so find max
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    # preserves heap structure
    if A[node] < A[child]:
        #__swap(A, node, child)
        A[node], A[child] = A[child], A[node]
        __siftdown(A, child)
    else:
        return

# runs in log(n) time    
def __siftup(A, node):
    '''Traverse up an otherwise max-heap `A` starting at node `node`
    (which is the only node that breaks the heap property) and restore 
    the heap structure.'''
    parent = (node - 1)/2
    if A[parent] < A[node]:
        #__swap(A, node, parent)
        A[node], A[parent] = A[parent], A[node]
    # base case; we've reached the top of the heap
    if parent <= 0:
        return
    else:
        __siftup(A, parent)
