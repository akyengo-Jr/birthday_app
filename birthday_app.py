import streamlit as st
from PIL import Image
import os
import base64

# --- Custom CSS ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%) !important;
    }
    .main {
        background: none !important;
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

# --- Welcome headline and confetti ---
st.balloons()
st.markdown("""
    <h1 style='text-align:center; font-size:3em; background: linear-gradient(90deg, #f9d423, #ff4e50); -webkit-background-clip: text; color: transparent;'>
        Happy Birthday! 🎉🎂
    </h1>
""", unsafe_allow_html=True)

# --- Prewritten birthday card message ---
st.markdown("""
<div style='display:flex; justify-content:center; margin-top:2em;'>
  <div style='background: #fffbe7; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); padding: 2em 3em; max-width: 500px; text-align: center;'>
    <h2 style='color:#ff4e50;'>Happy Birthday, Rachel!</h2>
    <p style='font-size:1.2em; color:#333;'>
        Girl, where do I even start? You’re the kind of friend who’s always there—whether I need a prayer, a pep talk, or just someone to laugh with (or at me when I’m being extra 😂). You’ve literally been helping me in every way I can think of—spiritually, financially, emotionally… you name it, you’ve helped me through it.<br><br>
        Today is all about YOU! I hope it’s filled with all the love, joy, and blessings you pour into everyone else’s lives. You deserve the world and more.<br>
        Thanks for being the realest, the kindest, and the absolute GOAT of friends. 🏆<br><br>
        Now go celebrate like the queen you are! 🥂💖<br><br>
        Love you loads! ❤️<br><br>
        P.S. Don’t worry, I got the cake (or wine, whichever you prefer 😉). Let’s turn up!<br><br>
        This app is a little messed up but I think you can manage 😂
    </p>
    <div style='font-size:2em;'>🎉🎁🍰</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Gallery Section: Fading Slideshow (Streamlit native) ---
st.subheader("Photo Gallery 📸")
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
if images:
    import time
    # Use Streamlit session state to keep track of current image
    if 'gallery_idx' not in st.session_state:
        st.session_state['gallery_idx'] = 0
    # Advance image every rerun (simulate fade by rerun)
    st.image(Image.open(os.path.join(gallery_folder, images[st.session_state['gallery_idx']])), use_column_width=True, caption=images[st.session_state['gallery_idx']], output_format="auto")
    time.sleep(2.5)
    st.session_state['gallery_idx'] = (st.session_state['gallery_idx'] + 1) % len(images)
    st.rerun()
else:
    st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")

# --- Music Section: Use st.audio for best compatibility ---
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
if music_files:
    selected_song = music_files[0]
    audio_path = os.path.join(music_folder, selected_song)
    audio_bytes = open(audio_path, "rb").read()
    st.audio(audio_bytes, format=None)  # Let Streamlit auto-detect format
    st.info("If music does not play automatically, please click the play button above. Some browsers require user interaction to start audio.")
