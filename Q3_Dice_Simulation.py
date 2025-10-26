import random

# Number of simulations
num_trials = 10000
count_sum_7 = 0

# Simulation of rolling two dice
for _ in range(num_trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1

# Estimated probability based on simulation
estimated_probability = count_sum_7 / num_trials

# Theoretical probability calculation
# Total favorable outcomes for sum of 7: 6 (1+6,2+5,3+4,4+3,5+2,6+1)
# Total outcomes with two dice: 6 * 6 = 36
theoretical_probability = 6 / 36

# Display results
print("Simulation Results:")
print(f"Total rolls: {num_trials}")
print(f"Number of times sum = 7: {count_sum_7}")
print(f"Estimated Probability: {estimated_probability:.4f}")

print("\nTheoretical Probability:")
print(f"6 / 36 = {theoretical_probability:.4f}")

print("\nComparison:")
difference = abs(estimated_probability - theoretical_probability)
print(f"Difference: {difference:.4f}")
