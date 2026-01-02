# streamlit_app_wordcount_fixed.py

import streamlit as st
from collections import Counter
import pandas as pd
import re

# ---------------- Helper Functions ----------------
# Basic stopwords (you can add more if needed)
STOPWORDS = {"about", "the", "and", "for", "with", "this", "that", "post", "tweet", "silver"}

def fetch_reddit_posts(topic, limit=50):
    # Simulate Reddit posts
    return [f"Reddit post about {topic} #{i+1}" for i in range(limit)]

def fetch_twitter_posts(topic, limit=50):
    return [f"Twitter tweet about {topic} #{i+1}" for i in range(limit)]

def fetch_facebook_posts(topic, limit=50):
    return [f"Facebook post about {topic} #{i+1}" for i in range(limit)]

def get_word_frequencies(posts):
    words = []
    for post in posts:
        # lowercase, remove numbers, hashtags, punctuation
        clean_post = re.sub(r'[^a-zA-Z\s]', '', post.lower())
        for word in clean_post.split():
            if word not in STOPWORDS:
                words.append(word)
    freq = Counter(words)
    df = pd.DataFrame(freq.items(), columns=["Word", "Count"])
    df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
    return df

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Social Media Word Counter", layout="wide")
st.title("Social Media Word Frequency Analyzer (Fixed)")

tab_reddit, tab_twitter, tab_facebook = st.tabs(["Reddit", "Twitter", "Facebook"])

# ------------- Reddit Tab -------------
with tab_reddit:
    st.header("Reddit Word Frequency")
    topic = st.text_input("Enter topic for Reddit:", "silver", key="reddit_topic")
    num_posts = st.slider("Number of posts to generate:", 10, 500, 50, step=10, key="reddit_slider")
    if st.button("Show Reddit Word Frequencies"):
        posts = fetch_reddit_posts(topic, num_posts)
        df = get_word_frequencies(posts)
        st.subheader("Top Words")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))

# ------------- Twitter Tab -------------
with tab_twitter:
    st.header("Twitter Word Frequency")
    topic = st.text_input("Enter topic for Twitter:", "silver", key="twitter_topic")
    num_posts = st.slider("Number of tweets to generate:", 10, 500, 50, step=10, key="twitter_slider")
    if st.button("Show Twitter Word Frequencies"):
        posts = fetch_twitter_posts(topic, num_posts)
        df = get_word_frequencies(posts)
        st.subheader("Top Words")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))

# ------------- Facebook Tab -------------
with tab_facebook:
    st.header("Facebook Word Frequency")
    topic = st.text_input("Enter topic for Facebook:", "silver", key="facebook_topic")
    num_posts = st.slider("Number of posts to generate:", 10, 500, 50, step=10, key="facebook_slider")
    if st.button("Show Facebook Word Frequencies"):
        posts = fetch_facebook_posts(topic, num_posts)
        df = get_word_frequencies(posts)
        st.subheader("Top Words")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))
