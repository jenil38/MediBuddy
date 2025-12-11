from flask import Flask, render_template, request, jsonify
from illness_logic import get_diagnosis

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    symptoms = request.form.getlist("symptoms")
    severities = request.form.getlist("severity")

    diagnosis_list = get_diagnosis(symptoms, severities)

    return render_template('result.html', symptoms=symptoms, diagnoses=diagnosis_list)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chatbot-response', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    user_message = data['message'].lower()

    # Simple rule-based reply logic
    if "fever" in user_message:
        reply = "It might be a viral infection. You can take Paracetamol 500mg."
    elif "cough" in user_message:
        reply = "Try taking Benadryl syrup. Drink warm fluids too."
    else:
        reply = "I'm still learning! Please describe more symptoms."

    return jsonify({'reply': reply})

# ✅ Only one run block
if __name__ == '__main__':
    app.run(debug=True)
