def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    maxsize = 0
    count = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if  j == len(A) - 1 or A[j] >= A[j+1] :
                size =  j - i + 1
                if size == maxsize:
                    count += 1
                elif size > maxsize:
                    maxsize = size
                    count = 1
                i = j + 1
                break
    print(count)
    return count
