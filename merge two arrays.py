# Function to merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    result = []  # Initialize an empty result list
    i, j = 0, 0  # Pointers for both arrays

    # Traverse both arrays and merge them
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])  # Add smaller element to result
            i += 1
        else:
            result.append(arr2[j])  # Add smaller element to result
            j += 1

    # Add any remaining elements from both arrays
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

# Example Usage
arr1 = [1, 4, 7]
arr2 = [2, 5, 6]
merged_array = merge_sorted_arrays(arr1, arr2)
print(f"Merged sorted array: {merged_array}")
