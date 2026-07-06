# Customer-Churn-Prediction

📌 Project Overview

This project predicts whether a customer will churn (leave) or stay using machine learning. The application is built with Python, Flask, Scikit-learn, and HTML/CSS and provides a simple web interface for user input and prediction.

📂 Project Structure

Customer_Churn_Prediction/

├── static/ # CSS, JS, images

├── templates/ # HTML templates

├── pycache/ # Python cache files

├── customer_churnNew1.csv # Dataset

├── customer_database.db # Database file

├── final_gb_classifier.pkl # Trained classifier model

├── regressor_model.pkl # Trained regression model

├── flask_app.py # Flask application

├── model.py # Model training script

├── req.txt # Requirements file

└── README.md # Project documentation

🚀 Features

Predict customer churn using a trained ML model.

Web interface built with Flask.

Uses Gradient Boosting Classifier.

Stores data in a local database.

Easy to run and test locally.

🛠️ Technologies Used

Python

Flask

Pandas

NumPy

Scikit-learn

Joblib

📥 Installation

1. Clone the repository

bash

git clone https://github.com/your-username/customer-churn-prediction.git

cd customer-churn-prediction

2. Install dependencies

bash

pip install -r req.txt

3. Run the Flask application

bash

python flask_app.py

4. Open in browser

http://127.0.0.1:5000/

📊 Model Information

File

	

Purpose




final_gb_classifier.pkl

	

Main churn prediction classifier




regressor_model.pkl

	

Regression-based prediction model

🧾 Requirements (req.txt)

Flask

pandas

numpy

scikit-learn

joblib

🎯 Future Improvements

Deploy on Render / Railway / Heroku.

Add user authentication.

Improve UI design.

Add model performance dashboard.

Use advanced ensemble models.

👩‍💻 Author

Ankita Shendge

Python Developer & Machine Learning Enthusiast

📜 License

This project is for educational and learning purposes.
