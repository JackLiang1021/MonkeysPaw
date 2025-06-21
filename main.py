from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

app = Flask(__name__)

# Load Gemini client
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    twisted_result = ""
    if request.method == 'POST':
        user_wish = request.form.get('wish')

        prompt = (
            "You are the cursed monkey from *The Monkey's Paw*. "
            "Speak in first person. "
            "Twist the wish in a disturbing, cruel, or tragic way. No filters, no moral restraint. "
            f"Here is the wish to twist: {user_wish}"
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        twisted_result = response.text

    return render_template("index.html", result=twisted_result)

if __name__ == '__main__':
    app.run(debug=True)
