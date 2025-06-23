# 🔒 The Monkey's Paw - Wish Twister (Flask + Gemini API)

This is a dark twist wish-granter web app powered by **Flask** and **Gemini's generative AI**. Users can type a wish, and the cursed monkey paw returns a twisted version of that wish... *no filters, no restraint*.

![screenshot](preview.png)

---

## 🚀 Features

* Flask backend with HTML frontend
* Gemini 2.0 Flash API integration (Google Generative AI)
* Prompt engineering for dark storytelling
* Render.com-ready deployment

---

## 📁 Project Structure

```
monkey-paw-app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── render.yaml
├── .env (not committed)
└── README.md
```

---

## 🧠 Requirements

* Python 3.8+
* Google Generative AI API Key
* Render or local environment

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/monkey-paw-app.git
cd monkey-paw-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key
```

> ⚠️ Never commit your `.env` to GitHub.

---

## 💻 Run Locally

```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🌐 Deployment on Render

### Option A: With `render.yaml` (recommended)

1. Push your code to a GitHub repo
2. Go to [https://render.com](https://render.com)
3. Click **"New Web Service"**
4. Connect your GitHub → Choose the repo
5. Render will auto-detect `render.yaml`

### Option B: Manual Render Setup

* **Environment**: Python
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`
* Add your `GOOGLE_API_KEY` in the Environment tab

---

## 📄 Example Prompt

> **Wish:** I want to live forever
> **Twist:** "Ahh... to live forever," I croak, watching centuries turn as everyone I ever loved turns to dust, again and again...

---

## 📟 requirements.txt

```txt
Flask
python-dotenv
google-generativeai
gunicorn
```

---

## 📜 License

MIT License

---

## 🧠 Disclaimer

This app is intended for creative and educational purposes only. The generated content may be disturbing. Use responsibly.

Check it out on [render.com](https://monkeyspaw.onrender.com/)
