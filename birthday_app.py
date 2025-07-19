import streamlit as st
from PIL import Image
import os
import time

# --- Gallery Section: Automatic Slideshow ---
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
if images:
    if 'gallery_idx' not in st.session_state:
        st.session_state['gallery_idx'] = 0
    img_path = os.path.join(gallery_folder, images[st.session_state['gallery_idx']])
    st.image(Image.open(img_path), use_container_width=True, caption=images[st.session_state['gallery_idx']])
    time.sleep(2.5)
    st.session_state['gallery_idx'] = (st.session_state['gallery_idx'] + 1) % len(images)
    st.rerun()  # <- Use st.rerun(), not st.experimental_rerun()
else:
    st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")

# --- Music Section: Show Audio Widget and Info ---
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
if music_files:
    selected_song = music_files[0]
    audio_path = os.path.join(music_folder, selected_song)
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    file_ext = os.path.splitext(selected_song)[1].lower()[1:]  # "mp3" or "wav"
    st.audio(audio_bytes, format=f"audio/{file_ext}")
    st.markdown("""
    <script>
    const aud = window.parent.document.querySelector('audio');
    if (aud) { aud.autoplay = true; aud.load(); aud.play(); }
    </script>
    """, unsafe_allow_html=True)
    st.info("Click the play button above to start the birthday music! Browsers block automatic audio playback for your privacy.")
else:
    st.info("No music files found in the 'music' folder. Please add .mp3 or .wav files.")
