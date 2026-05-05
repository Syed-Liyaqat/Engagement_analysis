import pandas as pd
import numpy as np

np.random.seed(42)

topics = ["Social Anxiety", "Dating", "Career Stress", "Loneliness", "Self Improvement", "Mental Health", "Friendship"]
formats = ["Short", "Long"]
times = ["Morning", "Afternoon", "Evening", "Night"]

n = 70
'''creating a dataset that follows a pattern where certain topics are more likely to get shares and saves, while others get more likes.
"Self Improvement" → higher saves
"Dating" → more shares
"Social Anxiety" → more comments
"Long format" → better retention
More engagement → higher retention,
this is patterns follows a realistic scenario based on typical social media performance which is easy to model and analyze in the dashboard, and perform statistical modelling and predictions based on the generated data.'''

rows = []

for i in range(n):
    topic = np.random.choice(topics)
    fmt = np.random.choice(formats)
    time = np.random.choice(times)

    base = np.random.randint(500, 2000)

    # Topic influence
    if topic == "Self Improvement":
        saves = base * np.random.uniform(0.8, 1.2)
        shares = base * np.random.uniform(0.4, 0.7)
    elif topic == "Dating":
        saves = base * np.random.uniform(0.4, 0.7)
        shares = base * np.random.uniform(0.8, 1.2)
    else:
        saves = base * np.random.uniform(0.5, 0.9)
        shares = base * np.random.uniform(0.5, 0.9)

    likes = base * np.random.uniform(1.5, 2.5)
    comments = base * np.random.uniform(0.1, 0.3)

    # Format effect
    if fmt == "Long":
        retention = 0.6 + 0.2 * np.random.rand()
    else:
        retention = 0.4 + 0.2 * np.random.rand()

    # Engagement boosts retention
    engagement_factor = (shares + saves) / (likes + 1)
    retention += 0.1 * engagement_factor

    retention = min(retention, 0.95)

    rows.append({
        "post_id": i+1,
        "topic": topic,
        "format": fmt,
        "post_time": time,
        "likes": int(likes),
        "shares": int(shares),
        "saves": int(saves),
        "comments": int(comments),
        "retention_rate": round(retention, 2)
    })

df = pd.DataFrame(rows)
df.to_csv("content_performance.csv", index=False)
