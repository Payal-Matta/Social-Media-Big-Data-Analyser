# streamlit_social_wordcloud.py

import streamlit as st
import pandas as pd
import feedparser
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# ---------------- Helper Functions ----------------

# Reddit fetch via RSS
def fetch_reddit_posts(topic, limit=100):
    url = f"https://www.reddit.com/r/all/search.rss?q={topic}&limit={limit}"
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    return titles if titles else ["No posts found"]

# Twitter placeholder (replace with API call)
def fetch_twitter_posts(topic, limit=100):
    st.warning("Twitter API not configured. Add your API keys and fetch logic.")
    return [f"Sample tweet about {topic}" for _ in range(limit)]

# Facebook placeholder (replace with API call)
def fetch_facebook_posts(topic, limit=100):
    st.warning("Facebook API not configured. Add your API keys and fetch logic.")
    return [f"Sample Facebook post about {topic}" for _ in range(limit)]

# Generate wordcloud from list of posts
def generate_wordcloud(posts):
    # Join all posts into one string
    text = " ".join(posts).lower()
    # Remove numbers, hashtags, punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    # Optional: remove some common stopwords
    stopwords = {"the","and","for","with","this","that","about","post","tweet","facebook","reddit","twitter"}
    words = [word for word in text.split() if word not in stopwords]
    text_clean = " ".join(words)
    
    if not text_clean.strip():
        return None
    
    wc = WordCloud(width=800, height=400, background_color="white").generate(text_clean)
    return wc

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Social Media Trending WordCloud", layout="wide")
st.title("Trending Words WordCloud Generator")

tab_fb, tab_reddit, tab_tw = st.tabs(["Facebook", "Reddit", "Twitter"])

# ---------------- Facebook Tab ----------------
with tab_fb:
    st.header("Facebook Trending WordCloud")
    topic_fb = st.text_input("Enter topic for Facebook:", "Bollywood", key="fb_topic")
    num_fb = st.slider("Number of posts to fetch:", 50, 1000, 200, step=50, key="fb_slider")
    if st.button("Generate Facebook WordCloud"):
        posts = fetch_facebook_posts(topic_fb, num_fb)
        wc = generate_wordcloud(posts)
        if wc:
            plt.figure(figsize=(12,6))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
        else:
            st.warning("No words to generate word cloud")

# ---------------- Reddit Tab ----------------
with tab_reddit:
    st.header("Reddit Trending WordCloud")
    topic_reddit = st.text_input("Enter topic for Reddit:", "Bollywood", key="reddit_topic")
    num_reddit = st.slider("Number of posts to fetch:", 50, 1000, 200, step=50, key="reddit_slider")
    if st.button("Generate Reddit WordCloud"):
        posts = fetch_reddit_posts(topic_reddit, num_reddit)
        wc = generate_wordcloud(posts)
        if wc:
            plt.figure(figsize=(12,6))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
        else:
            st.warning("No words to generate word cloud")

# ---------------- Twitter Tab ----------------
with tab_tw:
    st.header("Twitter Trending WordCloud")
    topic_tw = st.text_input("Enter topic for Twitter:", "Bollywood", key="tw_topic")
    num_tw = st.slider("Number of tweets to fetch:", 50, 1000, 200, step=50, key="tw_slider")
    if st.button("Generate Twitter WordCloud"):
        posts = fetch_twitter_posts(topic_tw, num_tw)
        wc = generate_wordcloud(posts)
        if wc:
            plt.figure(figsize=(12,6))
            plt.imshow(wc, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
        else:
            st.warning("No words to generate word cloud")
