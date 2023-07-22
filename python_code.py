# PROBLEM STATEMENT : -

# Given an array of integers and a number k, find maximum sum of a subarray of size k.

# EXAMPLES:-

'''
Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
'''


# BRUTE FORCE APPROACH

# In the naive method we are calculating the sum for every possible window and then finding the max which is a repetitive task.
# That's why it is increasing the time complexity

def maximumSumSubarray(arr, N, K):
    if N < K:
        return "INVALID WINDOW SIZE !!!"
    else:
        max_sum = -99999      # Initializing max_sum to a negative value
        for i in range(N-K+1):
            max_sum = max(max_sum, sum(arr[i:i + K]))    # Here we are repetitively calculating the sum of all windows.
        return max_sum


# TIME COMPLEXITY : O(N*K)
# SPACE COMPLEXITY : O(1)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# EFFICIENT APPROACH USING SLIDING WINDOW

# In this approach we'll not be repetitively calculating the sum of each window
# Rather we'll just calculate the sum of 1st window and then in the remaining windows we'll keep on
# subtracting the previous element and adding the current element

def maximumSumSubarraySlidingWindow(arr, N, K):
    if N < K:
        return "INVALID WINDOW SIZE !!!"
    else:
        max_sum = sum(arr[:K])    # Calculating the sum of 1st window of size K
        current_sum = max_sum
        for i in range(K,N):
            current_sum += arr[i] - arr[i-K]   # Adding the current element and removing the 1st element of the window from left.
            max_sum = max(max_sum, current_sum)
        return max_sum

# TIME COMPLEXITY : O(N-K)
# SPACE COMPLEXITY : O(1)

A = [100, 200, 300, 400]
K = 3
N = len(A)
#print(maximumSumSubarray(A,N,K)) # Uncomment this line if you want to try the brute force code
print(maximumSumSubarraySlidingWindow(A, N, K))


# Don't forget to star this repository if you are getting help from it and
# Any valid contribution is whole-heartedly welcomed  :-))
