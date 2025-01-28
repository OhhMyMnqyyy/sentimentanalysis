import streamlit as st
from transformers import pipeline

# Load pre-trained model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")

# Streamlit app title
st.title('Customer Review Sentiment Analysis')

# Add a text input for the customer review
review = st.text_area("Enter a customer review:")

if review:
    # Analyze sentiment
    sentiment = sentiment_analyzer(review)[0]
    
    # Display the result
    st.write(f"Sentiment: {sentiment['label']}")
    st.write(f"Confidence: {sentiment['score']:.2f}")
    
    # Color feedback based on sentiment
    if sentiment['label'] == 'POSITIVE':
        st.markdown('<h3 style="color:green;">The sentiment is positive! 😊</h3>', unsafe_allow_html=True)
    else:
        st.markdown('<h3 style="color:red;">The sentiment is negative! 😞</h3>', unsafe_allow_html=True)

