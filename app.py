import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
st.markdown("""
<style>
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:first-child {
    max-height: none !important;
    height: auto !important;
}
</style>
""", unsafe_allow_html=True)
st.title("Social Engagement Analytics Dashboard")
st.markdown("Data-Driven insights for content strategy")

df = pd.read_csv("data/content_performance.csv")
comments = pd.read_csv("data/comments.csv")

max_likes = df["likes"].max()
max_shares = df["shares"].max()
max_saves = df["saves"].max()
max_comments = df["comments"].max()
df["virality_coeff"] = 0.4*(df["shares"]/max_shares) + 0.3*(df["saves"]/max_saves) + 0.2*(df["likes"]/max_likes) + 0.1*(df["comments"]/max_comments)

# sidebar filter
st.sidebar.header("Filters")
selected_topic = st.sidebar.multiselect("Topic", df["topic"].unique(), default=df["topic"].unique())
filtered = df[df["topic"].isin(selected_topic)]

# metrics row
col1, col2, col3 = st.columns(3)
col1.metric("Total Posts", len(filtered))
col2.metric("Avg Virality Score", round(filtered["virality_coeff"].mean(), 3))
col3.metric("Top Topic", filtered.groupby("topic")["virality_coeff"].mean().idxmax())

# chart 1
st.subheader("Topic vs Virality Score")
fig1, ax1 = plt.subplots()
sns.barplot(data=filtered, x="topic", y="virality_coeff", ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

# chart 2
st.subheader("Format Comparison - A/B Test")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered, x="format", y="virality_coeff", ax=ax2)
st.pyplot(fig2)

# chart 3
st.subheader("Sentiment Distribution")
counts = comments["sentiments"].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(counts, labels=counts.index, autopct="%1.1f%%", colors=["steelblue","coral"])
st.pyplot(fig3)

# chart 4
st.subheader("Top 5 Posts by Virality")
st.dataframe(filtered.nlargest(5, "virality_coeff")[["post_id","topic","format","virality_coeff"]])

# chart 5 - trend
st.subheader("Trend Forecast — Next 4 Weeks")
weeks = ["Week 1","Week 2","Week 3","Week 4"]
topics_trend = ["Self Improvement","Career Stress","Dating","Loneliness","Social Anxiety"]
np.random.seed(79)
fig5, ax5 = plt.subplots()
for topic in topics_trend:
    trend = np.cumsum(np.random.uniform(0.05, 0.3, 4))
    ax5.plot(weeks, trend, marker="o", label=topic)
ax5.legend()
st.pyplot(fig5)