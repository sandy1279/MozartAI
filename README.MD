# 🎶 AI Music Generator 🎤🎸
---

## 🚀 Contribute to the Project

This is an open-source project, and **we're looking for contributors** passionate about:
- 🧠 LLM fine-tuning for creative tasks
- 🎼 Music and sound generation
- 🎨 Building creative AI tools
- 🖼️ Frontend/UX improvements
- 🔁 Integrating better TTS/music models
- 🧪 Testing and improving performance

### Want to Join?
1. 🍴 Fork the repository
2. 📥 Clone your fork
3. 🌱 Create a new branch for your feature or fix
4. ✅ Submit a Pull Request (PR)

Feel free to open an issue or discussion if you have ideas or want to collaborate!

> Contributions, feedback, and suggestions are **highly appreciated**! Let's build this together 🎵

## 💡 Idea Generation

I was inspired by how **musicians create songs** — first they **write lyrics**, then create **background music**, and finally **mix vocals** with instruments.

This project **mirrors that philosophy**, but with the power of **Generative AI** — automating the entire music creation pipeline.

Generate complete songs using AI — from **lyrics** to **vocals**, **background music**, and **final mix** — all in one pipeline.

Powered by:
- 🔥 Mistral (fine-tuned) for **lyric generation**
- 🎧 MusicGen for **instrumental audio**
- 🗣️ Bark for **vocal synthesis**
- 🎛️ PyDub for **audio mixing**
- ⚙️ FastAPI for backend API
- 🖼️ Streamlit for interactive frontend

---

## 🚀 Features

- Generate lyrics based on **genre**, **instruments**, and **mood**
- Convert lyrics into vocals using **text-to-speech**
- Compose background music matching theme and instruments
- Overlay vocals and music into a professional-sounding **final song**
- Export as `.mp3` or `.wav`

---



m### 📌 Code Summary

| File                  | Purpose |
|-----------------------|---------|
| `main.py`             | REST API server using FastAPI to call the pipeline from frontend |
| `pipeline.py`         | Main logic — from lyrics to music + vocal generation and final mix |
| `streamlit_app.py`    | User-friendly Streamlit interface to input prompts and listen to songs |
| `notebooks/mistral_finetune.ipynb` | Fine-tuning script for Mistral on lyrical dataset |
