from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 12,00,000"
    },
    {
        "id": 2,
        "title": "Backend Engineer",
        "location": "Remote",
        "salary": "Rs. 15,00,000"
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Delhi, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "location": "San Francisco, USA",
        "salary": "$120,000"
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)

@app.route("/job/<id>")
def show_job(id):
    job = None
    for j in JOBS:
        if str(j["id"]) == str(id):
            job = j
            break

    if not job:
        return "Job Not Found", 404

    return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
    job = None
    for j in JOBS:
        if str(j["id"]) == str(id):
            job = j
            break

    if not job:
        return "Job Not Found", 404

    application = request.form

    return render_template(
        "application_submitted.html",
        application=application,
        job=job
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)