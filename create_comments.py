#DELIVERABLE #2.2

import pandas as pd
import numpy as np

np.random.seed(42)

relatable_comments = [
    "this is literally me", "I feel so seen", "why is this so accurate",
    "nobody talks about this enough", "I needed to hear this today",
    "this hit different", "okay but why does this describe my life",
    "I'm crying this is so real", "sent this to my entire contact list",
    "this is the most relatable thing I've ever seen"
]

neutral_comments = [
    "interesting", "ok", "good content", "nice", "cool video",
    "thanks for sharing", "informative", "okay but why",
    "first", "more please"
]

rows = []
for post_id in range(1, 81):
    n_comments = np.random.randint(3, 8)
    for _ in range(n_comments):
        if np.random.rand() > 0.35:
            comment = np.random.choice(relatable_comments)
        else:
            comment = np.random.choice(neutral_comments)
        rows.append({"post_id": post_id, "comment_text": comment})

df = pd.DataFrame(rows)
df.to_csv("comments.csv", index=False)
print("done", len(df), "comments made")