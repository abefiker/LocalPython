def topKFrequent(nums, k):
    # Create a dictionary to store the frequency of each element in nums
    rd = {}

    # Count the occurrences of each element in nums
    for num in nums:
        if num in rd:
            rd[num] += 1
        else:
            rd[num] = 1

    # Sort the keys (elements) based on their frequencies in descending order
    sorted_elements = sorted(rd.keys(), key=lambda x: rd[x], reverse=True)

    # Return the first k elements from the sorted list
    return sorted_elements[:k]


# Example usage
arrs = [1, 1, 1, 2, 2, 3]
c = 2
print(topKFrequent(arrs, c))
