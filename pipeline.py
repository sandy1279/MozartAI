import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from bark import generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from pydub import AudioSegment

# === Load Models Once ===
print("🔁 Loading models...")
lyrics_model_path = "./mistral-lyrics-finetuned"
tokenizer = AutoTokenizer.from_pretrained(lyrics_model_path)
model = AutoModelForCausalLM.from_pretrained(lyrics_model_path, device_map="auto", torch_dtype=torch.float16)

music_model = MusicGen.get_pretrained("facebook/musicgen-small")
music_model.set_generation_params(duration=15)

preload_models()

# === Lyrics Generation ===
def generate_lyrics(genre, instruments, user_prompt):
    prompt = (
        f"You are a songwriting assistant. Write a {genre} song using {instruments} instruments. {user_prompt}"
    )
    input_text = f"<s>[INST] {prompt} [/INST]"
    inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

    output = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.9,
        top_p=0.95,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )
    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated.split("[/INST]")[-1].strip()

# === Music Generation ===
def generate_music(genre, instruments, mood, lyrics_excerpt):
    music_prompt = f"A {mood} {genre} song with {instruments}. Inspired by the theme: {lyrics_excerpt}"
    print("🎵 Generating background music...")
    wav = music_model.generate([music_prompt])
    audio_write("generated_music", wav[0].cpu(), sample_rate=32000)
    print("✅ Music saved as 'generated_music.wav'")

# === Vocals Generation ===
def generate_vocals(lyrics):
    print("🎤 Generating vocals from lyrics...")
    audio_array = generate_audio(lyrics)
    write_wav("vocal_output.wav", rate=24000, data=audio_array)
    print("✅ Vocals saved as 'vocal_output.wav'")

# === Mix Vocals + Music ===
def mix_audio():
    print("🎚️ Mixing vocals with background music...")
    bgm = AudioSegment.from_wav("generated_music.wav")
    vocals = AudioSegment.from_wav("vocal_output.wav")
    bgm = bgm - 5
    final_mix = bgm.overlay(vocals, position=0)
    final_mix.export("final_song.wav", format="wav")
    print("✅ Final song saved as 'final_song.wav'")

    # Convert to MP3
    song = AudioSegment.from_wav("final_song.wav")
    song.export("final_song.mp3", format="mp3")
    print("✅ Final song also saved as 'final_song.mp3'")

# === Main Pipeline ===
def process_music_pipeline(genre, instruments, mood, lyrics_prompt):
    print("\n🪄 Step 1: Generating Lyrics...")
    lyrics = generate_lyrics(genre, instruments, lyrics_prompt)
    print("🎶 Lyrics Generated:\n", lyrics)

    print("\n🪄 Step 2: Generating Music...")
    generate_music(genre, instruments, mood, lyrics[:100])

    print("\n🪄 Step 3: Generating Vocals...")
    generate_vocals(lyrics)

    print("\n🪄 Step 4: Mixing Vocals with Music...")
    mix_audio()

    print("\n🚀 All Done! Check the final_song.mp3 file in your directory.")

    return lyrics  # return lyrics for displaying in frontend
