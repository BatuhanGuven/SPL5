def calculate_mean(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    mean = total_sum / count
    return mean

def calculate_mean_with_two_decimal_places(numbers):
    mean = calculate_mean(numbers)
    mean_with_two_decimals = round(mean, 2)
    return mean_with_two_decimals


numbers = [1, 2, 3, 4, 5]
mean = calculate_mean(numbers)
mean_with_two_decimals = calculate_mean_with_two_decimal_places(numbers)

print(mean)
print(mean_with_two_decimals)
