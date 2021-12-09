# Bubble Sort
def bubble_sort(our_list):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
    return our_list

# Insertion Sort
def insertionSort(array):
    # iterate through the items in the unsorted array, i.e. all but the first item
    for i in range(1, len(array)):
        # iterate down through the sorted array + the first item in the unsorted array
        j = i
        # if the current item in this array is smaller than the next item, swap them
        while j > 0 and array[j] < array[j - 1]:
            # swap the two items in the array
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array
