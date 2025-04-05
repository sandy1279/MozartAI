import streamlit as st
import requests

st.set_page_config(page_title="Lyrics-to-Music Generator 🎵", layout="centered")

st.title("🎤 Lyrics-to-Music Generator")
st.markdown("Generate music from your ideas using AI!")

with st.form("music_form"):
    genre = st.selectbox("Select Genre", ["pop", "rock", "hiphop", "jazz", "lofi", "classical"])
    instruments = st.text_input("Instruments", value="guitar and piano")
    mood = st.text_input("Mood", value="romantic and chill")
    lyrics_prompt = st.text_area("Lyrics Theme", value="A song about falling in love on a rainy day.")

    submitted = st.form_submit_button("Generate Music 🎶")

if submitted:
    with st.spinner("Generating your song... hang tight! 🎧"):
        response = requests.post(
            "http://localhost:8000/generate-music/",
            data={
                "genre": genre,
                "instruments": instruments,
                "mood": mood,
                "lyrics_prompt": lyrics_prompt
            }
        )
        if response.status_code == 200:
            data = response.json()
            st.success("Done! Tap below to play your song 🎵")

            st.subheader("🎼 Generated Lyrics")
            st.write(data["lyrics"])

            st.subheader("🎧 Play Final Song")
            audio_file = requests.get("http://localhost:8000/get-song")
            with open("temp_final_song.mp3", "wb") as f:
                f.write(audio_file.content)
            st.audio("temp_final_song.mp3")

        else:
            st.error("Oops! Something went wrong. Check the backend.")
