# streamlit_app_basic.py

import streamlit as st
from collections import Counter

# ---------------- Helper Functions ----------------
def fetch_reddit_posts(topic, limit=20):
    # Placeholder data: no extra packages
    return [f"Reddit post about {topic} #{i+1}" for i in range(limit)]

def fetch_twitter_posts(topic, limit=20):
    return [f"Twitter tweet about {topic} #{i+1}" for i in range(limit)]

def fetch_facebook_posts(topic, limit=20):
    return [f"Facebook post about {topic} #{i+1}" for i in range(limit)]

def get_word_frequencies(posts):
    words = []
    for post in posts:
        words += post.lower().split()
    freq = Counter(words)
    return freq.most_common(20)  # top 20 words

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Simple Social Media WordCloud", layout="wide")
st.title("Simple Social Media Word Frequencies")

tab_reddit, tab_twitter, tab_facebook = st.tabs(["Reddit", "Twitter", "Facebook"])

# ------------- Reddit Tab -------------
with tab_reddit:
    st.header("Reddit Word Frequencies")
    topic = st.text_input("Enter topic for Reddit:", "silver", key="reddit_topic")
    num_posts = st.slider("Number of posts to generate:", 10, 100, 20, step=10, key="reddit_slider")
    if st.button("Show Reddit Word Frequencies"):
        posts = fetch_reddit_posts(topic, num_posts)
        freq = get_word_frequencies(posts)
        st.subheader("Top Words")
        for word, count in freq:
            st.write(f"{word}: {count}")

# ------------- Twitter Tab -------------
with tab_twitter:
    st.header("Twitter Word Frequencies")
    topic = st.text_input("Enter topic for Twitter:", "silver", key="twitter_topic")
    num_posts = st.slider("Number of tweets to generate:", 10, 100, 20, step=10, key="twitter_slider")
    if st.button("Show Twitter Word Frequencies"):
        posts = fetch_twitter_posts(topic, num_posts)
        freq = get_word_frequencies(posts)
        st.subheader("Top Words")
        for word, count in freq:
            st.write(f"{word}: {count}")

# ------------- Facebook Tab -------------
with tab_facebook:
    st.header("Facebook Word Frequencies")
    topic = st.text_input("Enter topic for Facebook:", "silver", key="facebook_topic")
    num_posts = st.slider("Number of posts to generate:", 10, 100, 20, step=10, key="facebook_slider")
    if st.button("Show Facebook Word Frequencies"):
        posts = fetch_facebook_posts(topic, num_posts)
        freq = get_word_frequencies(posts)
        st.subheader("Top Words")
        for word, count in freq:
            st.write(f"{word}: {count}")

