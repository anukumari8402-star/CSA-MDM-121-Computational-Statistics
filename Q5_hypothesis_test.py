import numpy as np
from scipy import stats

# Sample data (assumed)
class_A = [78, 85, 82, 90, 88, 76, 95, 89, 84, 91]
class_B = [72, 70, 68, 65, 74, 69, 71, 73, 67, 66]

# Step 1: Calculate means
mean_A = np.mean(class_A)
mean_B = np.mean(class_B)

# Step 2: Perform independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(class_A, class_B)

# Step 3: Display results
print("Class A Marks:", class_A)
print("Class B Marks:", class_B)
print("\nMean of Class A:", mean_A)
print("Mean of Class B:", mean_B)
print("\nT-statistic:", t_statistic)
print("P-value:", p_value)

# Step 4: Interpretation at 5% significance level
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject the null hypothesis (H0).")
    print("Interpretation: The average marks of the two classes are significantly different.")
else:
    print("\nResult: Fail to reject the null hypothesis (H0).")
    print("Interpretation: There is no significant difference in the average marks of the two classes.")