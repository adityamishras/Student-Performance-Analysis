# student_analysis.py

import matplotlib
matplotlib.use('Agg')  # Disable GUI backend (no Tkinter)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ✅ Ensure output directory exists
os.makedirs("charts", exist_ok=True)

# Step 1: Load Dataset
df = pd.read_csv("dataset/students_scores.csv")

# Step 2: View first few rows
print("✅ Dataset Preview:")
print(df.head(), "\n")

# Step 3: Basic Info
print("📊 Dataset Info:")
print(df.info(), "\n")

# Step 4: Descriptive Statistics
print("📈 Summary Statistics:")
print(df.describe(), "\n")

# Step 5: Missing Values
print("🚨 Missing Values:")
print(df.isnull().sum(), "\n")

# Step 6: Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png")
plt.close()

# Step 7: Study Hours vs Test Score
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Study_Hours', y='Test_Score', data=df, hue='Gender', s=60)
plt.title("Study Hours vs Test Score")
plt.tight_layout()
plt.savefig("charts/study_vs_score.png")
plt.close()

# Step 8: Attendance vs Test Score
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Attendance', y='Test_Score', data=df)
plt.title("Attendance vs Test Score")
plt.tight_layout()
plt.savefig("charts/attendance_vs_score.png")
plt.close()

# Step 9: Average Test Scores by Parent Education
plt.figure(figsize=(7, 4))
sns.barplot(x='Parent_Education', y='Test_Score', data=df, estimator='mean', ci=None)
plt.title("Average Test Score by Parent Education")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/parent_education_vs_score.png")
plt.close()

# Step 10: Insights Summary
print("🧠 --- Insights ---")
corr = df.corr(numeric_only=True)
print(f"1️⃣ Study hours correlate with test score: {corr.loc['Study_Hours', 'Test_Score']:.2f}")
print(f"2️⃣ Attendance correlates with test score: {corr.loc['Attendance', 'Test_Score']:.2f}")
print(f"3️⃣ Average test score: {df['Test_Score'].mean():.2f}")

print("\n✅ All plots saved in the 'charts/' folder.")
