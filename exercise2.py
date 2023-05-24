def calculate_mean(numbers, low_threshold=0, high_threshold=1):

    max_val = max(numbers)
    normalized_list = [round(item / max_val,2) for item in numbers]

    filtered_list = [item for item in normalized_list if low_threshold <= item <= high_threshold]


    total_sum = sum(filtered_list)
    count = len(filtered_list)
    mean = total_sum / count if count > 0 else 0

    return filtered_list, mean


numbers = [1, 2, 3]


filtered_values, mean = calculate_mean(numbers)

print("Input list:", numbers)
print("Normalized list:", filtered_values)


low_threshold = 0.5
high_threshold = 1
filtered_values, mean = calculate_mean(numbers, low_threshold, high_threshold)


print("Thresholds: low:", low_threshold, "high:", high_threshold)
print("Result output:", filtered_values)
print("Avg from normalized and filtered values:", round(mean,2))