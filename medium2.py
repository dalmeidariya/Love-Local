def find_elements(arr):
    n = len(arr)
    result = []
    for i in set(arr):
        if arr.count(i) > n // 3:
            result.append(i)
    return result
find_elements([1, 2, 3, 1, 2, 3, 1])
'''
1.Create an empty list result to store the elements that appear more than ⌊ n/3 ⌋ times.
2.Iterate over the set of unique elements in the array.
3.For each element, count the number of times it appears in the array using the count method.
4.If the count is greater than ⌊ n/3 ⌋, add the element to the result list.
5.Return the result list.'''