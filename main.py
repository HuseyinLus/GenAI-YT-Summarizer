import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptAvailable, VideoUnavailable

import torch
import gradio as gr
from transformers import pipeline

text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", 
                torch_dtype=torch.bfloat16)

def summary(input):
    output = text_summary(input)

    return output[0]['summary_text']

def extract_video_id(url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid URL")
    return match.group(1)

def get_youtube_transcript(url: str) -> str:
    try:
        video_id = extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item["text"] for item in transcript])
        return full_text
    except (TranscriptsDisabled, NoTranscriptAvailable, VideoUnavailable) as e:
        return f"Failed to extract Transcript: {str(e)}"
    except ValueError as ve:
        return f"URL Error: {str(ve)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"






gr.close_all()

demo = gr.Interface(
    fn=get_youtube_transcript,
    inputs=[gr.Textbox(label="Input YouTube URL to summarize", lines=1)],
    outputs=[gr.Textbox(label="Summarized text", lines=4)],
    title="@GenAILearniverse Project 2: YouTube Script Summarizer",
    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE YOUTUBE VIDEO SCRIPT."
)

demo.launch()