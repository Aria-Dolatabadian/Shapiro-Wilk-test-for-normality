import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, probplot
# Read the data from a CSV file (replace "data.csv" with your actual file name)
data = pd.read_csv("data.csv")
# Shapiro-Wilk test for normality
statistic, p_value = shapiro(data)
# Display the results
print(f"Shapiro-Wilk Statistic: {statistic}")
print(f"P-value: {p_value}")
# Interpret the results
alpha = 0.05  # Set your significance level
if p_value > alpha:
    print("The data does not appear to be normally distributed (fail to reject the null hypothesis)")
else:
    print("The data appears to be normally distributed (reject the null hypothesis)")
# Plot distribution, probability plot, and box plot
plt.figure(figsize=(16, 5))
# Distribution Plot
plt.subplot(1, 3, 1)
sns.histplot(data, kde=True)
plt.title('Distribution Plot')
# Probability Plot (Q-Q plot)
plt.subplot(1, 3, 2)
probplot(data.squeeze(), plot=plt)
plt.title('Probability Plot (Q-Q Plot)')
# Box Plot
plt.subplot(1, 3, 3)
sns.boxplot(data=data)
plt.title('Box Plot')
plt.tight_layout()
plt.show()

