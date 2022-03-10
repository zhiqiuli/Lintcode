def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        
        left  = array[   :mid]
        right = array[mid:   ]

        # Sort the left/right parts
        mergeSort(left )
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            # The value from the left half has been used
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        
        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)

runfile('/Users/zli/untitled1.py', wdir='/Users/zli')
[17, 20, 26, 31, 44, 54, 55, 77, 93]
