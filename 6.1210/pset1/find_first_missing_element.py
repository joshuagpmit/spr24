##################################################
##  Problem 4.d Oh, mamma mia!
##################################################

# Given a list of positive integers and the starting integer s, return x such that x is the smallest value greater than
# or equal to s that's not present in the list
def find_first_missing_element(arr, s):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        s          (int)       | Positive integer
    Output: 
        -          (int)       | The smallest integer greater than or equal to s that's not present in arr
    '''
    ##################
    # YOUR CODE HERE #
    ################## 
    if not arr:
        return s
    
    i = len(arr) // 2

    if arr[i] < s:
        return find_first_missing_element(arr[i+1:], s)
    
    else:
       k = arr[i] - s

       if i - k < 0:
           if arr[0] == s-i:
                return find_first_missing_element(arr[i+1:], arr[i] + 1)
       
           else:
                return find_first_missing_element(arr[:i], s)

       if arr[i-k] == s:
           return find_first_missing_element(arr[i+1:], arr[i] + 1)
       
       else:
           return find_first_missing_element(arr[:i], s)