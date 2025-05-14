import streamlit as st
from transformers import pipeline

# Title of the application
st.title("تحليل المشاعر للنصوص العربية")

# Text input field
text = st.text_area("📝 أدخل النص العربي هنا:")

# Button for sentiment analysis
if st.button("تحليل المشاعر"):
    # Load the sentiment analysis model
    sentiment_analysis = pipeline("sentiment-analysis", model="CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment")

    if text:
        # Perform sentiment analysis
        result = sentiment_analysis(text)[0]
        label = result['label']
        score = result['score']

        # Display results based on sentiment
        if "positive" in label.lower():
            st.success(f"رأي إيجابي 😊\nالدقة: {score:.2f}")
        elif "negative" in label.lower():
            st.error(f"رأي سلبي 😞\nالدقة: {score:.2f}")
        else:
            st.info(f"رأي محايد 😐\nالدقة: {score:.2f}")
    else:
        st.warning("يرجى إدخال نص أولاً.")


public_url = ngrok.connect(8501)
print("url", public_url)

!streamlit run app.py &>/dev/null &
