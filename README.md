# 💼 PayPredict — Salary Prediction System

An AI-powered web application that predicts employee salaries using Machine Learning. Built with **Flask**, **Python**, and **Scikit-Learn**, the system estimates annual salary based on job title, experience, education, skills, company size, and location.

---

## ✨ Features

- 🤖 **AI-Powered Prediction** — Random Forest Regression model trained on ~250,000 salary records
- 📝 **Smart Input Form** — enter job title, experience, education, skills count, company size, and location
- 📊 **Instant Results** — get an estimated annual salary in real time
- 🔐 **Admin Dashboard** — secure login panel to view prediction history and salary insights
- 🗄️ **Persistent Storage** — prediction records saved to a Neon (PostgreSQL) database
- 🎨 **Modern UI** — clean, responsive interface built with Bootstrap

---
## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

![Pickle](https://img.shields.io/badge/Pickle-FFD43B?style=for-the-badge&logo=python&logoColor=black)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Neon](https://img.shields.io/badge/Neon-00E599?style=for-the-badge&logo=postgresql&logoColor=black)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Bootstrap Icons](https://img.shields.io/badge/Bootstrap_Icons-8511FA?style=for-the-badge&logo=bootstrap&logoColor=white)|

---

## 📁 Project Structure

```
salary-ai/
├── app.py                     # Flask application & routes
├── model/
│   └── salary_model.pkl       # Trained Random Forest model
├── templates/
│   ├── index.html             # Landing page
│   ├── predict.html           # Salary prediction form
│   ├── about.html             # Project details page
│   ├── admin.html             # Admin dashboard
│   └── admin_login.html       # Admin login page
├── static/                    # CSS / JS / images (if applicable)
├── requirements.txt           # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/salary-ai.git
   cd salary-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=your_neon_postgres_connection_string
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=your_admin_password
   SECRET_KEY=your_flask_secret_key
   ```

5. **Run the application**
   ```bash
   flask run
   ```

   The app will be available at `http://127.0.0.1:5000`

---

## 🧠 How It Works

1. **User Input** — The user fills in employee details through the prediction form.
2. **Model Processing** — Flask sends the encoded input to the trained ML model.
3. **Salary Output** — The model returns a predicted annual salary, displayed instantly.
4. **Record Keeping** — Each prediction is saved to the database and visible in the admin dashboard.

**Input features used by the model:**
- Job Title
- Experience (Years)
- Education Level
- Skills Count
- Company Size
- Location

**Model performance:** R² Score ≈ **0.91** on the training dataset.

---

## 🔐 Admin Panel

The admin dashboard (`/admin`) provides:
- Total number of predictions made
- Highest, average, and most recent predicted salary
- A searchable log of all prediction records

Access is protected via `/admin_login` and requires valid admin credentials.

---

## 🚀 Future Improvements

- [ ] Add more granular location and role data
- [ ] Support salary prediction by currency/region
- [ ] Add data visualizations (charts/trends) to the admin dashboard
- [ ] Add REST API endpoints for third-party integration
- [ ] Add unit tests and CI/CD pipeline

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

Built by **[Your Name]** — feel free to connect or contribute!
