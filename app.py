from flask import Flask, render_template, request
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', bmi=None, bmr=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])/100
    age = int(request.form['age'])
    gender = request.form['gender']
    
    # Calculer le BMI et le BMR
    bmi = calculate_bmi(height, weight)
    bmr = calculate_bmr(height * 100, weight, age, gender)  # height en cm pour BMR
    
    # Renvoyer les résultats sur la même page
    return render_template('index.html', bmi=round(bmi, 2), bmr=round(bmr, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)