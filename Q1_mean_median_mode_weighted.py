from statistics import mean, median, mode

# Input dataset
data = [5, 3, 8, 3, 9, 5, 3, 7]
weights = [1, 2, 1, 1, 3, 1, 2, 1]  # Example weights for weighted mean

# Calculating Mean
mean_value = mean(data)

# Calculating Median
median_value = median(data)

# Calculating Mode
mode_value = mode(data)

# Calculating Weighted Mean
weighted_mean = sum(d * w for d, w in zip(data, weights)) / sum(weights)

# Display the results
print("Dataset:", data)
print("Weights:", weights)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Weighted Mean:", round(weighted_mean, 2))
