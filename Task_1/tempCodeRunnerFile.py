import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('Advanced Python/UScereal.csv')

# Bar Chart (2 variables) with custom color
plt.figure(figsize=(10, 6))
sns.barplot(x='Name', y='calories', data=df, color='skyblue')  
plt.title('Bar Chart (2 variables)')
plt.show()

# Bar Chart (3 variables) with custom color palette
plt.figure(figsize=(12, 8))
sns.barplot(x='Name', y='calories', hue='protein', data=df, palette='Set2')  
plt.title('Bar Chart (3 variables)')
plt.show()

# Scatter Plot (2 variables) with custom color
plt.figure(figsize=(10, 6))
plt.scatter(df['calories'], df['protein'], color='green')  
plt.title('Scatter Plot (2 variables)')
plt.xlabel('Calories')
plt.ylabel('Protein')
plt.show()

# Scatter Plot (3 variables) with custom color
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['calories'], df['protein'], df['fat'], c='red')  # Customize the color
ax.set_title('Scatter Plot (3 variables)')
ax.set_xlabel('Calories')
ax.set_ylabel('Protein')
ax.set_zlabel('Fat')
plt.show()

# Histogram (2 variables) with custom colors
plt.figure(figsize=(10, 6))
plt.hist([df['calories'], df['protein']], bins=10, alpha=0.7, label=['Calories', 'Protein'], color=['orange', 'purple'])  
plt.title('Histogram (2 variables)')
plt.legend()
plt.show()

# Histogram (3 variables) with custom colors
plt.figure(figsize=(12, 8))
plt.hist([df['calories'], df['protein'], df['fat']], bins=10, alpha=0.7, label=['Calories', 'Protein', 'Fat'], color=['green', 'blue', 'pink'])  # Customize the colors
plt.title('Histogram (3 variables)')
plt.legend()
plt.show()

# Pie Chart with custom colors
plt.figure(figsize=(8, 8))
plt.pie(df['calories'].value_counts(), labels=df['calories'].unique(), autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightgreen'])  # Customize the colors
plt.title('Pie Chart')
plt.show()

# Pair Plot with custom colors
sns.set(style="whitegrid")
sns.pairplot(df, palette='husl')  # Customize the color palette
plt.suptitle('Pair Plot')
plt.show()

# Bubble Plot with custom colors
plt.scatter(df['calories'], df['protein'], s=df['fat']*10, alpha=0.5, color='cyan')  # Customize the color
plt.title('Bubble Plot')
plt.xlabel('Calories')
plt.ylabel('Protein')
plt.show()

# Box Plot with custom colors
plt.figure(figsize=(10, 6))
sns.boxplot(x='calories', y='protein', data=df, color='purple')  # Customize the color
plt.title('Box Plot')
plt.show()

# Violin Plot with custom colors
plt.figure(figsize=(12, 8))
sns.violinplot(x='calories', y='protein', data=df, palette='pastel')  # Customize the color palette
plt.title('Violin Plot')
plt.show()

# Area Plot with custom color
plt.figure(figsize=(10, 6))
plt.fill_between(df['calories'], df['protein'], color='yellow', alpha=0.4)  # Customize the color
plt.title('Area Plot')
plt.xlabel('Calories')
plt.ylabel('Protein')
plt.show()

# Line Plot with custom color
plt.figure(figsize=(10, 6))
plt.plot(df['calories'], df['protein'], marker='o', color='brown')  # Customize the color
plt.title('Line Plot')
plt.xlabel('Calories')
plt.ylabel('Protein')
plt.show()