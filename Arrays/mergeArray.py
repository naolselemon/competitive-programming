def mergeArray(array1 ,array2) -> list:
    """
    take two arrays and return merged sorted result.
    Args:
        array1: List data type and first argument(sorted)
        array2: List data type and second argument(sorted)
    Returns:
        List: Merged sorted array
    """
    mergedArray = []
    i = j = 0
    while i < len(array1)  and j < len(array2):
        # The while is executed only when both array element exists
        if array1[i] < array2[j]:
            mergedArray.append(array1[i])
            i += 1
        else:
            mergedArray.append(array2[j])
            j += 1
        
    # if array1 has leftover elements add them at the end 
    if i < len(array1):
        mergedArray.extend(array1[i:])
    # if array2 has leftover elements add them at the end
    elif j < len(array2):
        mergedArray.extend(array2[j:])
     
    

    return mergedArray

print(mergeArray([1, 3,], [4,5, 6, 7]))