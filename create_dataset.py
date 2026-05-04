import pandas as pd
import numpy as np

np.random.seed(42)

topics = ["Social Anxiety", "Dating", "Career Stress", "Loneliness", "Self Improvement", "Mental Health", "Friendship"]
formats = ["Short", "Long"]
times = ["Morning", "Afternoon", "Evening", "Night"]

n = 80

df = pd.DataFrame({
    "post_id": range(1, n+1),
    "topic": np.random.choice(topics, n),
    "format": np.random.choice(formats, n),
    "post_time": np.random.choice(times, n),
    "likes": np.random.randint(200, 5000, n),
    "shares": np.random.randint(10, 800, n),
    "saves": np.random.randint(20, 1200, n),
    "comments": np.random.randint(5, 300, n),
    "retention_rate": np.round(np.random.uniform(0.3, 0.95, n), 2)
})

df.to_csv("content_performance.csv", index=False)
print("Done!", "\n", df.head())