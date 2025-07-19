import streamlit as st
from PIL import Image
import os
import json
import base64

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

# --- Auto-play and loop birthday music (hidden player) ---
music_folder = "music"
if not os.path.exists(music_folder):
    os.makedirs(music_folder)
music_files = [f for f in os.listdir(music_folder) if f.lower().endswith((".mp3", ".wav"))]
if music_files:
    selected_song = music_files[0]
    # For Streamlit Cloud, serve the file as a static asset
    audio_path = os.path.join(music_folder, selected_song)
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    st.markdown(f'''
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    ''', unsafe_allow_html=True)

# --- Gallery Section ---
st.subheader("Photo Gallery 📸")
gallery_folder = "gallery"
if not os.path.exists(gallery_folder):
    os.makedirs(gallery_folder)
images = [f for f in os.listdir(gallery_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
if images:
    import time
    import streamlit.components.v1 as components
    # Prepare base64 images for HTML
    import base64
    img_tags = []
    for img in images:
        img_path = os.path.join(gallery_folder, img)
        with open(img_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            img_tags.append(f'<img src="data:image/jpeg;base64,{b64}" class="fade-img" style="width:100%;max-width:500px;border-radius:20px;box-shadow:0 4px 20px rgba(0,0,0,0.2);margin-bottom:1em;display:none;"/>')
    # HTML/JS for fading slideshow
    html = f'''
    <style>
    .fade-img {{
        position: absolute;
        left: 0; right: 0;
        margin: auto;
        opacity: 0;
        transition: opacity 1s;
    }}
    .fade-img.active {{
        opacity: 1;
        position: relative;
        z-index: 2;
        display: block;
    }}
    .gallery-container {{
        position: relative;
        width: 100%;
        max-width: 500px;
        height: 350px;
        margin: auto;
    }}
    </style>
    <div class="gallery-container">
        {''.join(img_tags)}
    </div>
    <script>
    let idx = 0;
    const imgs = window.parent.document.querySelectorAll('.fade-img');
    if(imgs.length) {{
        imgs[0].classList.add('active');
        setInterval(() => {{
            imgs[idx].classList.remove('active');
            idx = (idx + 1) % imgs.length;
            imgs[idx].classList.add('active');
        }}, 2500);
    }}
    </script>
    '''
    components.html(html, height=370)
else:
    st.info("No pictures in the gallery yet. Add images to the 'gallery' folder.")
