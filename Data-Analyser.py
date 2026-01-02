# social_media_wordcloud_simulated.py

import streamlit as st
from collections import Counter
import pandas as pd
import re

# ---------------- Helper Functions ----------------
STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "about", "post", "tweet", 
    "facebook", "reddit", "twitter", "is", "in", "on", "to", "a"
}

# Simulated trending posts
def fetch_facebook_posts(topic, limit=50):
    sample = [
        f"{topic} news and latest updates",
        f"Fans reaction to {topic}",
        f"{topic} celebrity style and gossip",
        f"{topic} top trending videos",
        f"Upcoming {topic} movies and songs",
        f"{topic} events highlights",
        f"{topic} viral moments today",
        f"{topic} behind the scenes",
        f"{topic} interview with actor",
        f"Top {topic} songs and playlists"
    ]
    return (sample * (limit // len(sample) + 1))[:limit]

def fetch_reddit_posts(topic, limit=50):
    sample = [
        f"{topic} discussion thread trending now",
        f"Fans opinions about {topic}",
        f"{topic} memes and jokes",
        f"{topic} movie review",
        f"{topic} box office collection",
        f"{topic} news and updates",
        f"{topic} latest gossip",
        f"{topic} actor interviews",
        f"{topic} fan reactions",
        f"{topic} top posts today"
    ]
    return (sample * (limit // len(sample) + 1))[:limit]

def fetch_twitter_posts(topic, limit=50):
    sample = [
        f"Tweet about {topic} breaking news",
        f"Fans discuss {topic} latest updates",
        f"{topic} trending hashtag",
        f"{topic} viral tweet today",
        f"Reaction to {topic} announcement",
        f"{topic} top trending tweets",
        f"Celebrity news {topic}",
        f"{topic} memes and fun",
        f"{topic} fan reactions",
        f"{topic} viral video shared"
    ]
    return (sample * (limit // len(sample) + 1))[:limit]

def get_word_frequencies(posts):
    words = []
    for post in posts:
        clean_post = re.sub(r'[^a-zA-Z\s]', '', post.lower())
        for word in clean_post.split():
            if word not in STOPWORDS:
                words.append(word)
    freq = Counter(words)
    df = pd.DataFrame(freq.items(), columns=["Word", "Count"])
    df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
    return df.head(20)  # top 20 words

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Social Media Trending Words", layout="wide")
st.title("Trending Words Simulator (Facebook, Reddit, Twitter)")

tab_fb, tab_reddit, tab_tw = st.tabs(["Facebook", "Reddit", "Twitter"])

# ---------------- Facebook Tab ----------------
with tab_fb:
    st.header("Facebook Trending Words")
    topic_fb = st.text_input("Enter topic for Facebook:", "Bollywood", key="fb_topic")
    num_fb = st.slider("Number of posts to simulate:", 10, 500, 50, step=10, key="fb_slider")
    if st.button("Show Facebook Trending Words"):
        posts = fetch_facebook_posts(topic_fb, num_fb)
        df = get_word_frequencies(posts)
        st.subheader("Top Words on Facebook")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))

# ---------------- Reddit Tab ----------------
with tab_reddit:
    st.header("Reddit Trending Words")
    topic_reddit = st.text_input("Enter topic for Reddit:", "Bollywood", key="reddit_topic")
    num_reddit = st.slider("Number of posts to simulate:", 10, 500, 50, step=10, key="reddit_slider")
    if st.button("Show Reddit Trending Words"):
        posts = fetch_reddit_posts(topic_reddit, num_reddit)
        df = get_word_frequencies(posts)
        st.subheader("Top Words on Reddit")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))

# ---------------- Twitter Tab ----------------
with tab_tw:
    st.header("Twitter Trending Words")
    topic_tw = st.text_input("Enter topic for Twitter:", "Bollywood", key="tw_topic")
    num_tw = st.slider("Number of posts to simulate:", 10, 500, 50, step=10, key="tw_slider")
    if st.button("Show Twitter Trending Words"):
        posts = fetch_twitter_posts(topic_tw, num_tw)
        df = get_word_frequencies(posts)
        st.subheader("Top Words on Twitter")
        st.dataframe(df)
        st.bar_chart(df.set_index("Word"))
