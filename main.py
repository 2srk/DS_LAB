import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("edge_feasibility_data.csv")

# Convert 'yes/no' to binary
df['EdgeDeviceAvailable'] = df['EdgeDeviceAvailable'].map({'yes': 1, 'no': 0})

# Basic stats
print("Summary Statistics:")
print(df.describe(include='all'))

# Filter for feasible edge deployments
feasible = df[(df['Latency'] <= 20) &
              (df['Bandwidth'] >= 3) &
              (df['EdgeDeviceAvailable'] == 1) &
              (df['NetworkUptime'] >= 80)]

print(f"\nFeasible Edge Sites ({len(feasible)} locations):")
print(feasible[['Location', 'Latency', 'Bandwidth', 'PowerSource']])

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Latency', y='Bandwidth', hue='EdgeDeviceAvailable', size='NetworkUptime', style='PowerSource')
plt.title("Edge Feasibility: Latency vs Bandwidth")
plt.xlabel("Latency (ms)")
plt.ylabel("Bandwidth (Mbps)")
plt.grid(True)
plt.tight_layout()
plt.savefig("latency_vs_bandwidth.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix of Technical Metrics")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.show()
