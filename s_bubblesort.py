def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
mylist = [64, 34, 25, 12, 22, 90, 11]
print("Original List:", mylist)

bubble_sort(mylist)

print("Sorted List:",mylist)







def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
m_list = [112,45,27,45,34,90,756]
print("Unsorted list:",m_list)

bubble_sort(m_list)
print("sorted list:",m_list)