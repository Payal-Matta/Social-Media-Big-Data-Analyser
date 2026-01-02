# streamlit_app_bollywood.py

import streamlit as st
from collections import Counter
import pandas as pd
import re

# ---------------- Helper Functions ----------------
STOPWORDS = {"about", "the", "and", "for", "with", "this", "that", "post", "tweet", "is", "in", "on", "to", "a"}

# Simulated Bollywood posts
def fetch_bollywood_posts(topic, limit=100):
    sample_posts = [
        f"{topic} movie review trending now",
        f"{topic} box office hit",
        f"Latest {topic} news and gossip",
        f"{topic} actor interviews and behind the scenes",
        f"Fans reaction to {topic} songs",
        f"{topic} trailer released today",
        f"Upcoming {topic} movies 2026",
        f"{topic} celebrity fashion and style",
        f"{topic} award show highlights",
        f"Top {topic} songs playlist",
    ]
    # Repeat sample posts to simulate multiple entries
    return (sample_posts * (limit // len(sample_posts) + 1))[:limit]

def get_word_frequencies(posts):
    words = []
    for post in posts:
        # lowercase, remove numbers/punctuation
        clean_post = re.sub(r'[^a-zA-Z\s]', '', post.lower())
        for word in clean_post.split():
            if word not in STOPWORDS:
                words.append(word)
    freq = Counter(words)
    df = pd.DataFrame(freq.items(), columns=["Word", "Count"])
    df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
    return df.head(20)  # top 20 words

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Bollywood Trending Words", layout="wide")
st.title("Bollywood Trending Words Analyzer")

topic = st.text_input("Enter your topic:", "Bollywood")
num_posts = st.slider("Number of posts to analyze:", 50, 500, 100, step=10)

if st.button("Show Trending Words"):
    posts = fetch_bollywood_posts(topic, num_posts)
    df = get_word_frequencies(posts)
    
    st.subheader("Top Trending Words")
    st.dataframe(df)
    
    st.subheader("Trending Words Chart")
    st.bar_chart(df.set_index("Word"))
