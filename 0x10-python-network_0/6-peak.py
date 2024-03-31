def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int: A peak from the list.
    """

    # Helper function to perform binary search
    def binary_search(arr, low, high):
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return mid

        # If mid is not a peak and the left neighbor is greater, search left
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search(arr, low, mid - 1)

        # If mid is not a peak and the right neighbor is greater, search right
        else:
            return binary_search(arr, mid + 1, high)

    # Check for edge cases
    if not list_of_integers:
        return None

    # Perform binary search on the list
    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
