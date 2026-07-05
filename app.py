from flask import Flask, render_template, request
from database import init_db, load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career_connect.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)

    if not job:
        return "Job Not Found", 404

    return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
    job = load_job_from_db(id)

    if not job:
        return "Job Not Found", 404

    application = add_application_to_db(job.id, request.form)

    return render_template(
        "application_submitted.html",
        application=application,
        job=job
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)