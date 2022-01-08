#Find maximuFind maximum (or minimum) sum of a subarray of size km (or minimum) sum of a subarray of size k
# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

#Given
arr = [100,200,300,400]
k = 2 #window size



def max_sum_sub_array(arr,k):
    # initialization of variables
    i = 0
    j = 0
    current_sum = 0
    max_sum = 0

    while(j<len(arr)): #slide the window till the last element of an array
        current_sum = current_sum + arr[j] #temporary calculation within the window

        if(j-i+1) < k: # window size is still not hit, so increase j by one unit
            j +=1
        elif(j-i+1)==k: #when window size hit
            max_sum = max(max_sum,current_sum) #get one of the answer candidate
            current_sum = current_sum - arr[i] # calculation for sliding the window
            i +=1 # shift one unit of the window from start
            j +=1 #shift one unit of the window from end
    return max_sum


print(max_sum_sub_array(arr,k))