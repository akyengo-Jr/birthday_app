# Birthday App 🎉

A fun and interactive birthday app built with Python and Streamlit! The app welcomes the birthday girl with animations, lets her view a photo gallery, and allows friends to leave birthday wishes that persist after refresh.

## Features
- Animated, happy welcome screen
- Name and age input (required to access the main page)
- Balloons and cakes animation with a birthday message
- Photo gallery slideshow (add images to the `gallery` folder)
- Message section for friends to leave birthday wishes (persisted in `wishes.json`)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd birthday_app
```

### 2. Install Requirements
```sh
pip install -r requirements.txt
```

### 3. Add Gallery Images
Place your birthday photos in the `gallery` folder. Supported formats: `.jpg`, `.jpeg`, `.png`, `.gif`.

### 4. Run the App
```sh
streamlit run birthday_app.py
```

### 5. Using the App
- Enter the birthday girl's name and age to access the main page.
- View the photo gallery and slide through images.
- Leave a birthday wish in the message section. Wishes are saved and shown to everyone.

---

## Project Structure
```
birthday_app/
├── birthday_app.py
├── gallery/
│   └── (your images here)
├── wishes.json (auto-created)
├── requirements.txt
└── README.md
```

## Requirements
See `requirements.txt` for all dependencies.

## License
MIT
