import streamlit as st
import requests


st.title("🎬 YouTube Video Summarizer")

video_url = st.text_input("Enter YouTube URL:")

if st.button("Summarize"):
    if video_url:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://localhost:8000/api/summarize",
                    json={"url": video_url}
                )
                if response.status_code == 200:
                    st.success(response.json().get("summary"))
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to API: {e}")

