import pickle
import pandas as pd
from flask import Flask, render_template, request, redirect, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "salary_prediction_secret_key"

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_CHPGtB7Io9bw@ep-hidden-river-atnmwecb-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")


def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    return conn, cursor


# Load model and encoders
model = pickle.load(open("model/salary_model.pkl", "rb"))
job_encoder = pickle.load(open("model/job_encoder.pkl", "rb"))
edu_encoder = pickle.load(open("model/edu_encoder.pkl", "rb"))
company_encoder = pickle.load(open("model/company_encoder.pkl", "rb"))
location_encoder = pickle.load(open("model/location_encoder.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        job_title = request.form["job_title"]
        experience_years = int(request.form["experience_years"])
        education_level = request.form["education_level"]
        skills_count = int(request.form["skills_count"])
        company_size = request.form["company_size"]
        location = request.form["location"]

        job_encoded = job_encoder.transform([job_title])[0]
        edu_encoded = edu_encoder.transform([education_level])[0]
        company_encoded = company_encoder.transform([company_size])[0]
        location_encoded = location_encoder.transform([location])[0]

        input_data = pd.DataFrame([[
            job_encoded,
            experience_years,
            edu_encoded,
            skills_count,
            company_encoded,
            location_encoded
        ]], columns=[
            "job_title",
            "experience_years",
            "education_level",
            "skills_count",
            "company_size",
            "location"
        ])

        predicted_salary = model.predict(input_data)[0]
        prediction = f"{round(predicted_salary):,}"

        try:
            conn, cursor = get_db()
            cursor.execute("""
            INSERT INTO predictions
            (job_title, experience_years, education_level,
            skills_count, company_size, location, predicted_salary)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (
                job_title,
                experience_years,
                education_level,
                skills_count,
                company_size,
                location,
                prediction
            ))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"DB Error: {e}")

    return render_template(
        "predict.html",
        prediction=prediction,
        job_titles=job_encoder.classes_,
        education_levels=edu_encoder.classes_,
        company_sizes=company_encoder.classes_,
        locations=location_encoder.classes_
    )


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin")
        else:
            error = "Invalid username or password"

    return render_template("admin_login.html", error=error)


@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect("/admin-login")

    try:
        conn, cursor = get_db()
        cursor.execute("""
            SELECT *
            FROM predictions
            ORDER BY id ASC
        """)
        predictions = cursor.fetchall()
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")
        predictions = []

    total_predictions = len(predictions)
    highest_salary = 0
    average_salary = 0
    latest_prediction = 0

    if predictions:
        salaries = []
        for row in predictions:
            salary_value = int(str(row[7]).replace(",", ""))
            salaries.append(salary_value)

        highest_salary = max(salaries)
        average_salary = int(sum(salaries) / len(salaries))
        latest_prediction = salaries[0]

    return render_template(
        "admin.html",
        predictions=predictions,
        total_predictions=total_predictions,
        highest_salary=f"{highest_salary:,}",
        average_salary=f"{average_salary:,}",
        latest_prediction=f"{latest_prediction:,}"
    )


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
