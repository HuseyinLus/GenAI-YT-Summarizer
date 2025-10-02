import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled,NoTranscriptFound,VideoUnavailable

import torch
from transformers import pipeline

text_summary = pipeline(
    "summarization",
    model = "sshleifer/distilbart-cnn-12-6",
    torch_dtype=torch.bfloat16
)

def summary(text: str) -> str:
    output = text_summary(text)
    return output[0]['summary_text']


def extract_video_id(url:str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern,url)
    if not match:
        raise ValueError("Invalid URL")
    return match.group(1)

def get_youtube_transcript(url: str) -> str:
    try:
        video_id = extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item["text"] for item in transcript])
        return summary(full_text)
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        return f"Failed to extract Transcript: {str(e)}"
    except ValueError as ve:
        return f"URL Error: {str(ve)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

