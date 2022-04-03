from collections import deque
  
# Iterative function to print a complete binary search tree in increasing order
def printIncreasingOrder(keys):
 
    # base case
    if not keys:
        return
 
    # create a stack to store array indices
    s = deque()
 
    # start with the root node (the first array element)
    r = 0
 
    # push the root node into the stack
    s.append(r)
 
    # run till stack is empty
    while s:
 
        # push the left child of the current node into the stack
        # and repeat the same for the left child
        while r == s[-1] and r*2 + 1 < len(keys):
            r = r*2 + 1
            s.append(r)
 
        # print the last processed node and remove it from the stack
        r = s.pop()
        print(keys[r], end=' ')
 
        # push the right child of the current node into the stack
        if r*2 + 2 < len(keys):
            r = r*2 + 2
            s.append(r)
 
 
if __name__ == '__main__':
 
    keys = [15, 10, 20, 8, 12, 18, 25]
    printIncreasingOrder(keys)
 
