from typing import List, Optional

class AlgorithmicSolver:
    """A module containing fundamental algorithmic implementations."""

    @staticmethod
    def binary_search(arr: List[int], target: int) -> Optional[int]:
        """Implements Binary Search algorithm.
        
        Time Complexity: O(log n) | Space Complexity: O(1)
        Returns the index of target if found, else None.
        """
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return None

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """Solves the classic 'Two Sum' problem using a hash map.
        
        Time Complexity: O(n) | Space Complexity: O(n)
        Returns indices of the two numbers that add up to the target.
        """
        seen = {}  # value -> index
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
            
        return []

# --- Demonstration of the Module ---
if __name__ == "__main__":
    solver = AlgorithmicSolver()

    # Test Binary Search (Array must be sorted)
    sorted_data = [10, 23, 45, 70, 11, 15]
    sorted_data.sort() 
    target_val = 45
    
    print(f"Searching for {target_val} in sorted array: {sorted_data}")
    idx = solver.binary_search(sorted_data, target_val)
    print(f"Element found at index: {idx}\n")

    # Test Two Sum
    numbers = [2, 7, 11, 15]
    target_sum = 9
    print(f"Finding indices for target sum {target_sum} in {numbers}...")
    indices = solver.two_sum(numbers, target_sum)
    print(f"Indices: {indices}")