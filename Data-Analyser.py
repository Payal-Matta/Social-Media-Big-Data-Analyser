# streamlit_app.py

import streamlit as st
import pandas as pd
import feedparser
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ---------------- Helper Functions ----------------
def fetch_reddit_posts(topic, limit=500):
    url = f"https://www.reddit.com/r/all/search.rss?q={topic}&limit={limit}"
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    return titles if titles else ["No posts found."]

def fetch_twitter_posts(topic, limit=500):
    # Placeholder: Replace with Twitter API logic
    st.warning("Twitter API not configured. Add your API keys and fetching code.")
    return [f"Sample tweet about {topic}"] * limit

def fetch_facebook_posts(topic, limit=500):
    # Placeholder: Replace with Facebook API logic
    st.warning("Facebook API not configured. Add your API keys and fetching code.")
    return [f"Sample Facebook post about {topic}"] * limit

def generate_wordcloud(text_list):
    if not text_list:
        return None
    df = pd.DataFrame(text_list, columns=["text"])
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["text"])
    scores = tfidf_matrix.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    tfidf_dict = dict(zip(words, scores))
    wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(tfidf_dict)
    return wc

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Social Media WordCloud Generator", layout="wide")
st.title("Social Media WordCloud Generator")

# Tabs
tab_reddit, tab_twitter, tab_facebook = st.tabs(["Reddit", "Twitter", "Facebook"])

# ------------- Reddit Tab -------------
with tab_reddit:
    st.header("Reddit WordCloud")
    topic_reddit = st.text_input("Enter topic for Reddit:", "silver", key="reddit_topic")
    num_posts_reddit = st.slider("Number of posts to fetch:", 500, 5000, 1000, step=100, key="reddit_slider")
    if st.button("Generate Reddit WordCloud"):
        with st.spinner("Fetching Reddit posts..."):
            posts = fetch_reddit_posts(topic_reddit, limit=num_posts_reddit)
            wc = generate_wordcloud(posts)
            if wc:
                plt.figure(figsize=(12,6))
                plt.imshow(wc, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("No data to generate word cloud.")

# ------------- Twitter Tab -------------
with tab_twitter:
    st.header("Twitter WordCloud")
    topic_twitter = st.text_input("Enter topic for Twitter:", "silver", key="twitter_topic")
    num_posts_twitter = st.slider("Number of tweets to fetch:", 500, 5000, 1000, step=100, key="twitter_slider")
    if st.button("Generate Twitter WordCloud"):
        with st.spinner("Fetching Twitter posts..."):
            posts = fetch_twitter_posts(topic_twitter, limit=num_posts_twitter)
            wc = generate_wordcloud(posts)
            if wc:
                plt.figure(figsize=(12,6))
                plt.imshow(wc, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("No data to generate word cloud.")

# ------------- Facebook Tab -------------
with tab_facebook:
    st.header("Facebook WordCloud")
    topic_facebook = st.text_input("Enter topic for Facebook:", "silver", key="facebook_topic")
    num_posts_facebook = st.slider("Number of posts to fetch:", 500, 5000, 1000, step=100, key="facebook_slider")
    if st.button("Generate Facebook WordCloud"):
        with st.spinner("Fetching Facebook posts..."):
            posts = fetch_facebook_posts(topic_facebook, limit=num_posts_facebook)
            wc = generate_wordcloud(posts)
            if wc:
                plt.figure(figsize=(12,6))
                plt.imshow(wc, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("No data to generate word cloud.")
