import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# # Load training and test datasets
data = pd.read_csv("train.csv")
# test_df = pd.read_csv("test.csv")

# # Display basic info
# print(train_df.info())
# print(test_df.info())

# #Check for Missing Values
# missing_values = train_df.isnull().sum().sort_values(ascending=False)
# missing_values = missing_values[missing_values > 0]  # Only show columns with missing values
# print(missing_values)

# #Check Class Distribution of target
# sns.countplot(x=train_df['target'])
# plt.title("Distribution of Malware Infections (Target Variable)")
# plt.show()

# #Check Basic Statistics
# print(train_df.describe())  # Summary statistics for numerical features
# print(train_df.describe(include='object'))  # Summary for categorical features

#To find the number of unique OS versions in the dataset, we use:
unique_os_versions = data['OSVersion'].nunique()
print("Unique OS Versions:", unique_os_versions)

#To determine the maximum value of this feature:
max_antivirus_products = data['NumAntivirusProductsInstalled'].max()
print("Maximum NumAntivirusProductsInstalled:", max_antivirus_products)

#Systems owned by gamers where malware was detected:
malware_detected_in_gamers = data[(data['IsGamer'] == 1) & (data['target'] == 1)].shape[0]
print("Malware detected in systems owned by gamers:", malware_detected_in_gamers)


#For systems with IsPassiveModeEnabled = 1, find the most frequent value
most_frequent_realtime_state = data[data['IsPassiveModeEnabled'] == 1]['RealTimeProtectionState'].mode()[0]
print("Most frequent RealTimeProtectionState where IsPassiveModeEnabled=1:", most_frequent_realtime_state)


#Identify systems with the specific resolution
screen_resolution_count = data[
    (data['PrimaryDisplayResolutionHorizontal'] == 1366) &
    (data['PrimaryDisplayResolutionVertical'] == 768)
].shape[0]
print("Number of systems with resolution 1366x768:", screen_resolution_count)


#The 50th percentile of TotalPhysicalRAMMB:
median_ram = data['TotalPhysicalRAMMB'].median()
print("50th Percentile (Median) of TotalPhysicalRAMMB:", median_ram)

##Exploratory Data Analysis (EDA)

#Feature Correlation:
# Filter numeric columns
numeric_data = data.select_dtypes(include=['number'])

# Handle missing values (alternative: use mean/median imputation)
numeric_data = numeric_data.fillna(numeric_data.median())  

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

# Plot the correlation matrix
plt.figure(figsize=(15, 10))  # Increase figure size for better visibility
sns.heatmap(correlation_matrix, cmap='coolwarm', center=0, square=True, linewidths=0.5)
plt.title('Correlation Matrix', fontsize=14)
plt.show()


# #Missing Values: Visualize missing values:
# sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
# plt.title("Missing Values Heatmap")
# plt.show()


# #Feature Distributions: Use histograms or box plots for numerical features:
# data['TotalPhysicalRAMMB'].hist(bins=30)
# plt.title("Distribution of TotalPhysicalRAMMB")
# plt.xlabel("RAM (MB)")
# plt.ylabel("Count")
# plt.show()


# #Categorical Feature Analysis: For features like IsGamer, use count plots:
# sns.countplot(data['IsGamer'])
# plt.title("Distribution of Gamers")
# plt.show()








# # Show first few rows
# train_df.head()
