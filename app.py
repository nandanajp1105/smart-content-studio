from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# -------- CONTENT DATA --------
content_data = {
    "fitness": [
        ("Morning workout routine", "Start your day strong 💪", "#fitness #gym #health"),
        ("Fat loss tips", "Burn smarter, not harder 🔥", "#fatloss #fitness"),
        ("Quick home workout", "No excuses today!", "#homeworkout #fitlife")
    ],
    "fashion": [
        ("Streetwear ideas", "Style that speaks 😎", "#fashion #style"),
        ("Minimal outfits", "Less is more ✨", "#ootd #minimal"),
        ("Summer outfits", "Stay cool ☀️", "#summerfashion #trendy")
    ],
    "tech": [
        ("Top AI tools", "Work smarter 🤖", "#ai #tools"),
        ("Best apps 2026", "Upgrade your phone 📱", "#apps #tech"),
        ("Hidden tech hacks", "You didn’t know this 😮", "#tech #hacks")
    ],
    "business": [
        ("Startup tips", "Build smart 💼", "#startup #business"),
        ("Marketing hacks", "Grow faster 📈", "#marketing #growth"),
        ("Brand building", "Create identity 🔥", "#branding")
    ]
}

# -------- ROUTES --------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generator')
def generator():
    return render_template('generator.html')

@app.route('/analyzer')
def analyzer():
    return render_template('analyzer.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# -------- GENERATE CONTENT --------
@app.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.json
    niche = data['niche']

    idea, caption, hashtags = random.choice(
        content_data.get(niche, content_data["fitness"])
    )

    return jsonify({
        "idea": idea,
        "caption": caption,
        "hashtags": hashtags
    })

# -------- ANALYZER --------
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    likes = int(data['likes'])
    comments = int(data['comments'])
    followers = int(data['followers'])

    engagement = ((likes + comments) / followers) * 100

    status = "Good" if engagement > 5 else "Average"

    return jsonify({
        "engagement": round(engagement, 2),
        "status": status
    })

# -------- BEST TIME --------
@app.route('/best-time')
def best_time():
    return jsonify({
        "time": "Best time to post: 7PM - 9PM"
    })

# -------- RUN --------
if __name__ == '__main__':
    app.run(debug=True)