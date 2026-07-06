# app.py
from flask import Flask, render_template, request, send_file
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import sqlite3
import os

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        return render_template('form.html')

    elif request.method == 'POST':

        gender = int(request.form.get('gender'))
        age = int(request.form.get('age'))
        tenure = int(request.form.get('tenure'))
        monthly = float(request.form.get('monthlyCharges'))
        total = float(request.form.get('totalCharges'))
        payment = int(request.form.get('paymentMethod'))
        contract = int(request.form.get('contractType'))
        internet = int(request.form.get('internetService'))
        streaming = int(request.form.get('streamingServices'))
        tech = int(request.form.get('techSupport'))

        score = 0

        if age > 50:
            score += 2
        if tenure < 12:
            score += 2
        if monthly > 70:
            score += 2
        if tech == 0:
            score += 2
        if contract == 0:
            score += 2

        if score >= 6:
            result = "LIKELY TO LEAVE"
            probability = 85
            risk = "HIGH RISK"
        elif score >= 3:
            result = "MODERATE RISK"
            probability = 60
            risk = "MEDIUM RISK"
        else:
            result = "LIKELY TO STAY"
            probability = 20
            risk = "LOW RISK"

        return render_template(
            'output.html',
            result=result,
            probability=probability,
            risk=risk
        )
# =========================
# DASHBOARD
# =========================
@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect('customer_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        probability REAL
    )
    ''')

    conn.commit()

    cursor.execute('SELECT probability FROM predictions')
    data = cursor.fetchall()

    probabilities = [x[0] for x in data]

    if len(probabilities) == 0:
        probabilities = [10, 20, 30, 40]

    plt.figure(figsize=(6,4))
    plt.plot(probabilities)

    plt.title('Customer Churn Probability')
    plt.xlabel('Customers')
    plt.ylabel('Probability')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    graph_path = os.path.join(BASE_DIR, 'static', 'graph.png')

    plt.savefig(graph_path)
    plt.close()

    conn.close()

    return render_template('dashboard.html')

# =========================
# DOWNLOAD REPORT
# =========================

# =========================
# RUN APPdef download_report():
# =========================
# DOWNLOAD REPORT
# =========================
@app.route('/download_report')
def download_report():

    from reportlab.pdfgen import canvas

    pdf_path = os.path.join(app.root_path, 'static', 'report.pdf')

    c = canvas.Canvas(pdf_path)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, 800, "Customer Churn Prediction Report")

    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "Prediction Result: LIKELY TO STAY")
    c.drawString(100, 720, "Probability: 85%")
    c.drawString(100, 690, "Risk Level: LOW RISK")

    c.save()

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name='Customer_Report.pdf'
    )
# =========================
if __name__ == '__main__':
    app.run(debug=True)@app.route('/download_report')
