import streamlit as st
from PIL import Image
import os
import json

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%);
        color: #fff;
    }
    .stButton>button {
        background-color: #ff4e50;
        color: white;
        border-radius: 20px;
        font-size: 18px;
        padding: 0.5em 2em;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #f9d423;
        font-size: 18px;
    }
    .stSlider>div>div>div {
        background: #f9d423;
    }
    .gallery-img {
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome headline
st.markdown("""
    <h1 style='text-align:center; font-size:3em; background: linear-gradient(90deg, #f9d423, #ff4e50); -webkit-background-clip: text; color: transparent;'>
        Happy Birthday! 🎉🎂
    </h1>
""", unsafe_allow_html=True)

# Confetti on entry
st.balloons()

# Prewritten birthday card message
st.markdown("""
<div style='display:flex; justify-content:center; margin-top:2em;'>
  <div style='background: #fffbe7; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); padding: 2em 3em; max-width: 500px; text-align: center;'>
    <h2 style='color:#ff4e50;'>Happy Birthday, [Name]!</h2>
    <p style='font-size:1.2em; color:#333;'>
      Wishing you a day filled with laughter, love, and all your favorite things.<br>
      May your year ahead sparkle with joy and bring you wonderful memories.<br>
      Enjoy your special day to the fullest! 🎈🎂💖
    </p>
    <div style='font-size:2em;'>🎉🎁🍰</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Music Player ---
st.subheader("🎵 Birthday Music")
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
if music_files:
    selected_song = st.selectbox("Pick a song to play:", music_files)
    audio_bytes = open(os.path.join(music_folder, selected_song), 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')
else:
    st.info("Add mp3 or wav files to the 'music' folder to play birthday songs!")

# --- Gallery Section ---
st.subheader("Photo Gallery 📸")
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
if images:
    img_idx = st.slider("Slide through the gallery", 0, len(images)-1, 0)
    img_path = os.path.join(gallery_folder, images[img_idx])
    st.image(Image.open(img_path), use_column_width=True, caption=images[img_idx], output_format="auto")
else:
    st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")
