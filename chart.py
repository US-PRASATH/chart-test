# chart.py
# Generates chart.png (512x512) using seaborn lineplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reproducible data
rng = np.random.default_rng(42)
x = np.arange(0, 50)
y = np.sin(x / 5) + 0.2 * rng.normal(size=len(x))
df = pd.DataFrame({"x": x, "y": y})

# 512x512 px: figsize(inches)*dpi = pixels => 5.12*100 = 512
fig = plt.figure(figsize=(5.12, 5.12), dpi=100)
ax = fig.add_subplot(111)

sns.lineplot(data=df, x="x", y="y", ax=ax)

ax.set_title("Seaborn Line Plot (512x512)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, linewidth=0.5, alpha=0.3)

fig.savefig("chart.png", dpi=100)  # exact 512x512
plt.close(fig)
