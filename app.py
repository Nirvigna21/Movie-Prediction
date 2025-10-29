from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hero = float(request.form['hero'])
        director = float(request.form['director'])
        budget = float(request.form['budget'])
        script = float(request.form['script'])
        marketing = float(request.form['marketing'])

        # simple logic — acts like a fake ML model 😎
        score = (0.3*hero + 0.25*director + 0.2*script + 0.15*marketing + 0.1*(budget/100))
        result = "Hit 🎉" if score >= 5 else "Flop 💔"

        return render_template('index.html', prediction=f"The movie is predicted as a {result}")
    except:
        return render_template('index.html', prediction="Error! Please enter valid numbers.")

if __name__ == '__main__':
    app.run(debug=True)
