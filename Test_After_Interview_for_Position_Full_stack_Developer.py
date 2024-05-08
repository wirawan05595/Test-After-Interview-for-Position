def merge_arrays_unique(arr1, arr2):
    arr_all = arr1 + arr2
    result = []
    
    for i in arr_all:
        if i not in result:
            result.append(i)
    
    return result

def remove_duplicates(arr1, arr2):
    arr_all = arr1 + arr2
    intersection = set(arr1) & set(arr2)
    result = []
    
    for i in arr_all:
        if i not in intersection:
            result.append(i)
    
    return result

array1 = ['a', 'b', 'c']
array2 = ['b', 'c', 'd']

answer1 = merge_arrays_unique(array1, array2)
answer2 = remove_duplicates(array1, array2)

print("Merged array without duplicates:", answer1)
print("Merged array with duplicates removed:", answer2)
