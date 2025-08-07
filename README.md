# YouTube Transcript Summarizer

This project extracts and summarizes the transcript of any YouTube video using Hugging Face transformers.

## 🚀 Features

- 📥 Automatically fetches transcript from a YouTube video (if available)
- 🧠 Summarizes the transcript using `distilbart-cnn-12-6`
- 🖥️ Simple user interface built with Gradio

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/youtube-transcript-summarizer.git
cd youtube-transcript-summarizer

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install -r requirements.txt
