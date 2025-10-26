data = [10, 20, 20, 40, 50]

# 1) Range
data_min = min(data)
data_max = max(data)
data_range = data_max - data_min

# 2) Mean (μ)
mean_value = sum(data) / len(data)

# 3) Squared differences: (x_i - μ)^2
squared_diffs = [(x - mean_value) ** 2 for x in data]

# 4) Variance
# Population variance: σ^2 = sum((x_i - μ)^2)/N
population_variance = sum(squared_diffs) / len(data)

# Sample variance: s^2 = sum((x_i - μ)^2)/(N - 1)
sample_variance = sum(squared_diffs) / (len(data) - 1)

# 5) Standard deviation
# Population std dev: σ = sqrt(σ^2)
population_std = population_variance ** 0.5

# Sample std dev: s = sqrt(s^2)
sample_std = sample_variance ** 0.5

# ---- Display step-by-step results ----
print("Dataset:", data)
print("\n--- Range ---")
print(f"Min: {data_min}, Max: {data_max}, Range: {data_range}")

print("\n--- Mean ---")
print(f"Mean (μ): {mean_value}")

print("\n--- Squared differences (x_i - μ)^2 ---")
for i, (x, sd) in enumerate(zip(data, squared_diffs), start=1):
    print(f"x{i} = {x:>3} -> (x{i} - μ)^2 = {sd}")

print("\n--- Variance ---")
print(f"Population variance (σ^2) = sum(squared_diffs)/N = {sum(squared_diffs)} / {len(data)} = {population_variance}")
print(f"Sample variance (s^2)     = sum(squared_diffs)/(N-1) = {sum(squared_diffs)} / {len(data)-1} = {sample_variance}")

print("\n--- Standard deviation ---")
print(f"Population std dev (σ) = sqrt(σ^2) = {population_std}")
print(f"Sample std dev (s)     = sqrt(s^2) = {sample_std}")