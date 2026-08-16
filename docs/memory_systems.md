# Memory Systems in Foundation Agents

Effective intelligence requires a structured approach to memory that goes beyond simple vector databases. The Foundation Agent Architecture (FAA) implements a memory hierarchy inspired by the human hippocampus and neocortex.

## 1. Memory Taxonomy

The framework categorizes memory into three distinct types:
- **Working Memory:** Short-term, high-access storage for current task state and immediate observations.
- **Episodic Memory:** A version-controlled history of past experiences, successes, and failures.
- **Semantic Memory:** Long-term storage of general knowledge, facts, and fixed operational rules.

## 2. The Importance-Weighted Decay Logic

To maintain context efficiency, the FAA uses an importance-weighted decay model. Every memory object is assigned an **Importance Score (I)** between 0 and 1. The retention probability **(R)** over time **(t)** is calculated as:

$$R = e^{-\frac{t}{S \cdot I}}$$

Where **S** is the base strength of the memory system. This ensures that core strategic reflections are preserved while transient noise is automatically pruned.

## 3. Implementation Example (Python)

```python
import time
import math

class MemoryObject:
    def __init__(self, content, importance):
        self.content = content
        self.importance = importance # 0.0 to 1.0
        self.created_at = time.time()

    def get_retention_score(self, base_strength=50):
        elapsed = time.time() - self.created_at
        # Ebbinghaus Forgetting Curve
        return math.exp(-elapsed / (base_strength * self.importance))

# High importance memory (Strategy)
core_goal = MemoryObject("Reduce token cost by 40%", importance=0.9)

# Low importance memory (Log)
temp_log = MemoryObject("HTTP 200 OK from API", importance=0.1)
```
