from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from pipeline import process_music_pipeline  # 👈 External modular pipeline logic
import os

app = FastAPI()

@app.post("/generate-music/")
def generate_music(
    genre: str = Form(...),
    instruments: str = Form(...),
    mood: str = Form(...),
    lyrics_prompt: str = Form(...)
):
    lyrics = process_music_pipeline(genre, instruments, mood, lyrics_prompt)
    return {"lyrics": lyrics, "status": "success"}

@app.get("/get-song/")
def get_song():
    if os.path.exists("final_song.mp3"):
        return FileResponse("final_song.mp3", media_type="audio/mpeg", filename="final_song.mp3")
    return {"error": "Song not found"}
