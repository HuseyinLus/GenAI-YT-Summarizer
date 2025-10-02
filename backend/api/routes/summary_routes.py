from fastapi import APIRouter
from pydantic import BaseModel
from core.pipeline import get_youtube_transcript

router = APIRouter(prefix="/summarize", tags=["summarize"])

class YoutubeURL(BaseModel):
    url: str

@router.post("/summarize_video")
def summarize(url):
    result = get_youtube_transcript(url)
    return{"answer": result}