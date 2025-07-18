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

# Input for name and age
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'age' not in st.session_state:
    st.session_state['age'] = 0
if 'entered' not in st.session_state:
    st.session_state['entered'] = False

if not st.session_state['entered']:
    with st.form("birthday_form"):
        name = st.text_input("What's your name?")
        age = st.number_input("How old are you today?", min_value=1, max_value=120, step=1)
        submitted = st.form_submit_button("Enter")
        if submitted and name and age:
            st.session_state['name'] = name
            st.session_state['age'] = age
            st.session_state['entered'] = True
            st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

if st.session_state['name'] and st.session_state['age'] and st.session_state['entered']:
    st.balloons()
    st.markdown(f"<h2 style='text-align:center;'>Happy {st.session_state['age']}th Birthday, {st.session_state['name']}! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Wishing you a day filled with love, laughter, and cake! 🍰</h4>", unsafe_allow_html=True)

    # --- Customizable Themes ---
    theme = st.selectbox("Choose a theme:", ["Sunshine", "Party", "Ocean", "Classic"])
    theme_colors = {
        "Sunshine": ("#f9d423", "#ff4e50"),
        "Party": ("#ff6f61", "#6a0572"),
        "Ocean": ("#43cea2", "#185a9d"),
        "Classic": ("#fff", "#333")
    }
    bg1, bg2 = theme_colors[theme]
    st.markdown(f"""
        <style>
        .main {{background: linear-gradient(135deg, {bg1} 0%, {bg2} 100%);}}
        </style>
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

    # --- Sidebar Navigation ---
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "Gallery", "Wishes"])

    if page == "Gallery":
        st.header("Photo Gallery 📸")
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

    elif page == "Wishes":
        st.header("🎈 Birthday Wishes")
        st.info("Birthday wishes are not being accepted at this time. Enjoy the gallery and music!")

    else:
        st.info("Welcome to the birthday app! Use the sidebar to view the gallery or leave a wish.")
else:
    st.info("Please enter your name and age to continue.")
