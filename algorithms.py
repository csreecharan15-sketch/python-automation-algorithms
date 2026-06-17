def binary_search(item_list, target):
    """Standard binary search implementation."""
    low = 0
    high = len(item_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if item_list[mid] == target:
            return mid
        elif item_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Return -1 if element is not found

def find_two_sum(numbers, target_sum):
    """Finds indices of two numbers that add up to the target."""
    seen_numbers = {}  # Stores number as key and its index as value
    
    for i in range(len(numbers)):
        current_num = numbers[i]
        needed_num = target_sum - current_num
        
        if needed_num in seen_numbers:
            return [seen_numbers[needed_num], i]
        
        seen_numbers[current_num] = i
        
    return []

# Testing the functions
if __name__ == "__main__":
    # Test Binary Search (List must be sorted)
    my_list = [10, 15, 23, 30, 45, 70]
    target = 45
    print("Searching for", target, "in", my_list)
    print("Found at index:", binary_search(my_list, target))
    print()

    # Test Two Sum
    nums_array = [2, 7, 11, 15]
    total = 9
    print("Finding pair for total", total, "in", nums_array)
    print("Indices:", find_two_sum(nums_array, total))