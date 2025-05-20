import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("g-search .csv")

# Top 5 queries by clicks
top = df.sort_values("Clicks", ascending=False).head(5)
print("Top 5 by Clicks:\n", top[['Query', 'Clicks']])

# Avg CTR & Position
print("\nAvg CTR:", round(df['CTR'].mean(), 3))
print("Avg Pos:", round(df['Position'].mean(), 2))

# High potential: CTR>0.1 and Position > 5
hp = df[(df['CTR'] > 0.1) & (df['Position'] > 5)]
print("\nHigh Potential:\n", hp[['Query', 'CTR', 'Position']])

# Bar chart of Top Queries
top.plot(kind="bar", x="Query", y="Clicks", color="skyblue")
plt.title("Top 5 Queries by Clicks")
plt.ylabel("Clicks")
plt.tight_layout()
plt.savefig("top_queries.png")
plt.show()

# Scatter Plot: Position vs CTR
plt.scatter(df['Position'], df['CTR']*100, color='green')
plt.title("CTR vs Position")
plt.xlabel("Position (Lower is Better)")
plt.ylabel("CTR (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("ctr_vs_position.png")
plt.show()