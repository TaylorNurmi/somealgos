def longestPeak(array):
    current_peak_len = 1
    longest_peak = 0
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            current_peak_len = 3
            left = i - 2
            right = i + 2
            while left >= 0 and array[left] < array[left + 1]:
                current_peak_len += 1
                left -= 1
            while right < len(array) and array[right] < array[right - 1]:
                current_peak_len += 1
                right += 1
            longest_peak = max(longest_peak, current_peak_len)
        elif array[i] > array[i - 1]:
            current_peak_len += 1
        else:
            current_peak_len = 1
    return longest_peak
