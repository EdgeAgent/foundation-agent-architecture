import matplotlib.pyplot as plt
import numpy as np

# Time steps (e.g., hours or days)
t = np.linspace(0, 100, 500)

# Ebbinghaus-style Forgetting Curve: R = e^(-t/S)
# S is the strength of memory
high_importance = np.exp(-t / 80)
medium_importance = np.exp(-t / 30)
low_importance = np.exp(-t / 10)

plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

ax.plot(t, high_importance, label='High Importance (Core Strategy)', color='#10b981', linewidth=2.5)
ax.plot(t, medium_importance, label='Medium Importance (Task Context)', color='#3b82f6', linewidth=2)
ax.plot(t, low_importance, label='Low Importance (Transient Logs)', color='#ef4444', linewidth=1.5, linestyle='--')

ax.set_xlabel('Time Elapsed (Relative Units)', fontsize=12, fontweight='bold')
ax.set_ylabel('Memory Retention Probability', fontsize=12, fontweight='bold')
ax.set_title('Brain-Inspired Memory Lifecycle: Importance-Weighted Decay', fontsize=14, fontweight='bold', pad=15)
ax.legend(frameon=True, fontsize=10)
ax.set_ylim(0, 1.1)

# Highlight the "Consolidation" phase
ax.fill_between(t, 0, 1.1, where=(t < 20), color='gray', alpha=0.1, label='Consolidation')
ax.text(5, 0.05, 'Initial Encoding', fontsize=9, color='gray', fontstyle='italic')

plt.tight_layout()
plt.savefig('/home/ubuntu/foundation-agent-architecture/assets/memory_decay_lifecycle.png')
plt.close()
print("Memory decay chart generated.")
